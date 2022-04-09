# py-economy
A simple to use economy module.
WARNING: This project is in alpha release and may be unstable and buggy.
Developers: Konrad (@konradsic)
## Install
```pip install pyeconomy==0.1.0```
## Version
Currently running on version 0.1.0
## Links
* [PyPi - Python Package Index](https://pypi.org)
## How it works
It is very simple:
* Everything is stored in `.json` files
* Discord async functions works as same normal, but it returns an embed object that you can send.
## Code example:
```py
import pyeconomy as economy
instance = economy.Ecoomy(discord_mode=False, dir="./json/economy/")

user = instance.get_user_by_id(id="1234567890") # enter user id here
print(f"{user.name}'s balance: {user.balance}")
```
This easy example will create an economy instance (`economy.Economy`) set discord mode to `False` and directory of `.json` files in `./json/economy/`
Then it searches for a user with id `124542323` and prints it's balance.
