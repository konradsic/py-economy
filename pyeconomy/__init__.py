"""
py-economy
~~~~~~~~~~~~~~
Copyright (c) 2022 Konrad (@konradsic)
Under the MIT License, see LICENSE file for more details.
"""

import typing as t
from errors import *
import os

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
            raise InvalidParameter("'dir' argument is required")
        if not os.path.has_valid_dir_syntax(dir):
            raise OSError(f"\"{dir}\" is not a valid directory syntax")
        self._discord = discord_mode
        self._dir = dir