from database import create_account, login


def register():
    username = input("Username: ")
    password = input("Password: ")

    if create_account(username, password):
        print("Account created.")
    else:
        print("Username already exists.")


def user_login():
    username = input("Username: ")
    password = input("Password: ")

    return login(username, password)