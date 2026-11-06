from items import items


def shop_menu(player):

    while True:

        print("\nSHOP")

        for item in items:
            print(item, "-", items[item]["cost"])

        print("0 Exit")

        choice = input("> ")

        if choice == "0":
            break

        if choice in items:

            cost = items[choice]["cost"]

            if player.gold >= cost:
                player.gold -= cost
                player.inventory.append(choice)
                print("Purchased.")
            else:
                print("Not enough gold.")