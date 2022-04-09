"""
py-economy
~~~~~~~~~~~~~~
Copyright (c) 2022 Konrad (@konradsic)
Under the MIT License, see LICENSE file for more details.
"""

import typing as t

class Economy:
    """
    Represents the basic Economy class

    Arguments
    --------------------
        discord_mode: :class:`bool`
            Used for easier use in discord
            This is an optional argument. Default is `False`
        dir: :class:`str`
            Directory where all data is stored.
    """
    def __init__(
        self,
        discord_mode: bool = False,
        dir: str = None
    ) -> None:
        if discord_mode:
            import discord
        if not dir:
            raise OSError("'dir' arguments is a required argument")