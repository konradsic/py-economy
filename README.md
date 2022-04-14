# py-economy
<a href="https://pypi.org/project/pyeconomy/0.1.26/"><img src="https://shields.io/pypi/v/pyeconomy.svg" alt="pypi_version" /></a>
<a href="https://pypi.org/project/pyeconomy/0.1.26/"><img src="https://img.shields.io/pypi/pyversions/pyeconomy.svg" alt="python_supported_versions" /></a>

A simple to use economy module.
WARNING: This project is in alpha release and may be unstable and buggy.
Developers: Konrad (@konradsic)
## Install
```pip install pyeconomy```
## Links
* [PyPi - Python Package Index](https://pypi.org/project/pyeconomy/0.1.26/)
## How it works
It is very simple:
* Everything is stored in `.json` files
* Discord async functions works same as normal, but it returns an embed object that you can send.
## Code example:
```py
import pyeconomy as economy
instance = economy.Economy(discord_mode=False)

user = instance.get_user_by_id(id="1234567890") # enter user id here
if user is None:
    print("User not found!")
else:
    print(f"{user.name}'s balance: {user.wallet}")
```
This easy example will create an economy instance (`economy.Economy`) set discord mode to `False`.
Then it searches for a user with id `1234567890`, checks if it exists and prints it's balance.
Please note, that its an pre-alpha relase and it does not support discord yet. 
