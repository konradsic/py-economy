"""
py-economy
~~~~~~~~~~~~~~
Copyright (c) 2022 Konrad (@konradsic)
Under the MIT License, see LICENSE file for more details.
"""

__version__ = "0.1.26"

from .json_data import *
from .types.user import EconomyUser, update_user, create_user
from .errors import InvalidParameter, ValueOutOfRange, EconomyException

class Economy:
    """
    Represents the basic Economy class

    Arguments
    --------------------
        discord_mode: :class:`bool`
            Used for easier use in discord
            This is an optional argument. Default is `False`

    WARNING: All files are stored in `./economy` directory
    """
    def __init__(
        self,
        discord_mode: bool = False,
    ) -> None:
        if discord_mode:
            import discord
        create_economy_files()
        self._discord = discord_mode
        self.data = self._get_data()

    def _get_data(self) -> None:
        return json_data.load_json_file("economy_data.json")

    def get_user_by_id(self, id: str = None) -> EconomyUser:
        """
        Returns economy user if it exists

        Arguments
        ---------
            id: :class:`str`
                ID of the user

        Returns
        ---------
            user: :class:`EconomyUser`
                The user if it exists
            None:
                Returns None if the user does not exist
        """
        try:
            user = EconomyUser()
            user.name = self.data[id]["name"]
            user.id = id
            user.created_at = self.data[id]["created_at"]
            user.wallet = self.data[id]["wallet"]
            user.bank = self.data[id]["bank"]
            return user
        except:
            return None

    def withdraw(self, user : EconomyUser, amount: int) -> EconomyUser:
        """
        Withdraws user's money

        Arguments
        ---------
            user: :class:`EconomyUser`
                The user to withdraw money from.
            amount: :class:`int`
                The money to withdraw
        
        Returns
        ---------
            new_user: :class:`EconomyUser`
                The user with updated parameters.
        
        Raises
        ---------
            InvalidParameter:
                Raised when type of the user is not supported
            ValueOutOfRange:
                Raised when the amount is out of range.
        """
        if not isinstance(user, EconomyUser):
            raise InvalidParameter(f"Parameter \"{user}\" must be of type Economy user, not {type(user)}")
        if not 0 <= amount <= user.bank:
            raise ValueOutOfRange("Amount out of range")
        
        user.bank = int(user.bank) - int(amount)
        user.wallet = int(user.wallet) + int(amount)

        update_user(user)

        return user
    
    
    def deposit(self, user : EconomyUser, amount : int) -> EconomyUser:
        """
        Deposits user's money

        Arguments
        ---------
            user: :class:`EconomyUser`
                The user to deposit money from.
            amount: :class:`int`
                The money to deposit
        
        Returns
        ---------
            new_user: :class:`EconomyUser`
                The user with updated parameters.
        
        Raises
        ---------
            InvalidParameter:
                Raised when type of the user is not supported
            ValueOutOfRange:
                Raised when the amount is out of range.
        """
        if not isinstance(user, EconomyUser):
            raise InvalidParameter(f"Parameter \"{user}\" must be of type Economy user, not {type(user)}")
        if not 0 <= amount <= user.wallet:
            raise ValueOutOfRange("Amount out of range")
        
        user.wallet = int(user.wallet) - int(amount)
        user.bank = int(user.bank) + int(amount)

        update_user(user)

        return user

    def display_money_with(money : str, what : str) -> str:
        """
        Displays money with given parameter

        Parameters
        -----------
            money: :class:`str`
                String, amount of Money
            what: :class:`str`
                String, what to replace with
        
        Returns
        -----------
            money: :class:`str`
                New string with replacement.
        """
        money = str(money)
        return f"{money:,}".replace(",", what)