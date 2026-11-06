from auth import register, user_login
from player import Player
from game import game_loop
from database import save_player

print("===== ELDORIA RPG =====")

while True:

    print("\n1 Register")
    print("2 Login")
    print("3 Exit")

    choice = input("> ")

    if choice == "1":
        register()

    elif choice == "2":

        account = user_login()

        if account:

            player = Player(account)

            game_loop(player)

            save_player(player)

        else:
            print("Login Failed")

    elif choice == "3":
        break