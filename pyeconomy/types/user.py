"""
MIT License

Copyright (c) 2022 Konrad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from turtle import update
import typing as t
from ..json_data import load_json_file, save_json_file
import time

class EconomyUser:
    """
    Represents a Economy User

    Parameters
    ------------
        name: :class:`str`
            The name of the user
        id: :class:`str`
            The id of the user
        created_at: :class:`float`
            The name of the user
        wallet: :class:`str`
            Money in the wallet of the user
        bank: :class:`str`
            Bank balance of the user
    """
    name: str = ""
    id: str = ""
    created_at: float = 0.0 # time.time()
    wallet: str = "0"
    bank: str = "0"

def generate_id(name: str) -> str:
    time_ = time.time()
    def numerize():
        nonlocal name
        ret = ""
        for c in name:
            ret += str(ord(c))
        return int(ret)
    name = numerize()
    retID = str(round(name*time_))
    retID = retID[:15]
    if (len(retID) < 15):
        retID += ("0" * (15-len(retID)))

    return retID

def create_user(name: str):
    """
    Creates a new economy user

    Parameters
    ------------
        name: :class:`str`
            The name of the user

    Returns
    ------------
        user: :class:`EconomyUser`
            The new, created user

    """
    user = EconomyUser()
    user.name = name
    user.id = generate_id(name)
    user.created_at = time.time()
    user.wallet = "10000"
    user.bank = "0"
    update_user(user)

def update_user(user: EconomyUser):
    data = load_json_file("economy_data.json")
    data[str(user.id)] = {
        "name": user.name,
        "id": user.id,
        "created_at": user.created_at,
        "wallet": user.wallet,
        "bank": user.bank
    }
    save_json_file("economy_data.json", data)