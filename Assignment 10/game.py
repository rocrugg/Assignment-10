from maps import village, show_map
from quests import show_current_quest
from inventory import show_inventory
from shop import shop_menu


def game_loop(player):

    while True:

        print("\n===== MENU =====")
        print("1 Map")
        print("2 Inventory")
        print("3 Quest")
        print("4 Shop")
        print("5 Character")
        print("6 Save & Exit")

        choice = input("> ")

        if choice == "1":
            show_map(village)

        elif choice == "2":
            show_inventory(player)

        elif choice == "3":
            show_current_quest(player)

        elif choice == "4":
            shop_menu(player)

        elif choice == "5":

            print(player.username)
            print("Level:", player.level)
            print("XP:", player.xp)
            print("Gold:", player.gold)

        elif choice == "6":
            break