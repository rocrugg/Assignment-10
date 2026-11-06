from random import randint


def battle(player, monster):

    print(f"A wild {monster.name} appears!")

    while monster.hp > 0 and player.hp > 0:

        print()
        print("Player HP:", player.hp)
        print("Enemy HP:", monster.hp)

        choice = input(
            "1-Attack 2-Run: "
        )

        if choice == "1":

            damage = randint(10, 20)

            monster.hp -= damage

            print("You dealt", damage)

        elif choice == "2":
            return

        if monster.hp > 0:

            player.hp -= monster.attack

            print(
                monster.name,
                "hits for",
                monster.attack
            )

    if player.hp > 0:

        print(
            "Victory!"
        )

        player.gold += monster.gold

        player.gain_xp(50)

    else:

        print("Game Over")