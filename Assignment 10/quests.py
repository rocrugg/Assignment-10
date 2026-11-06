main_quests = {

    0: "Talk to Village Elder",

    1: "Collect Ancient Relic",

    2: "Defeat Dragon",

    3: "Defeat Malzor"
}


def show_current_quest(player):
    print(main_quests[player.main_quest])