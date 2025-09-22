username = input("Please enter username:\n").strip()
password = input("Please enter your password:\n").strip()


if username and password:
    print(f"Welcome!{username.title()}")
    print(f"Your password is {password}")
elif username and (not password):
    print("You didn't enter your password!")
elif (not username) and password:
    print("You didn't enter your username!")
else:
    print("You didn't enter username and password!")