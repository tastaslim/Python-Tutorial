userName = input("Enter user name: ")
password = input("Enter password: ")
password_length = len(password)
if password_length > 6:
    print(
        f"Length is greater than 6. Your user name {userName}, password is {password} and hidden password is {'*'*password_length}")
elif password_length < 6:
    print(
        f"Length is 6. Your user name {userName}, password is {password} and hidden password is {'*'*password_length}")
else:
    print(
        f"Length is less than 6. Your user name {userName}, password is {password} and hidden password is {'*'*password_length}")
