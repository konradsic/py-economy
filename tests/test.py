import pyeconomy as economy

obj = economy.Economy(discord_mode=False)

user = obj.get_user_by_id("123")

if not user:
    print("No user!")
    exit()

print(f"{user.name}'s balance: {user.wallet}")