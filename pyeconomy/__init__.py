"""
py-economy
~~~~~~~~~~~~~~
Copyright (c) 2022 Konrad (@konradsic)
Under the MIT License, see LICENSE file for more details.
"""

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
        self._discord = discord_mode