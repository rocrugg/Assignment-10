items = {
    "Potion": {
        "heal": 25,
        "cost": 15
    },

    "Super Potion": {
        "heal": 50,
        "cost": 30
    },

    "Mega Potion": {
        "heal": 75,
        "cost": 50
    }
}


def use_item(player, item_name):

    if item_name not in player.inventory:
        return

    if item_name in items:
        heal = items[item_name]["heal"]

        player.hp += heal

        if player.hp > player.max_hp:
            player.hp = player.max_hp

        player.inventory.remove(item_name)

        print(f"Recovered {heal} HP")