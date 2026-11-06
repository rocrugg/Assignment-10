from tinydb import TinyDB, Query

db = TinyDB("save_data.json")

users = db.table("users")

User = Query()


def create_account(username, password):
    if users.search(User.username == username):
        return False

    users.insert({
        "username": username,
        "password": password,
        "level": 1,
        "xp": 0,
        "gold": 50,
        "hp": 100,
        "max_hp": 100,
        "inventory": ["Potion"],
        "skills": ["Slash"],
        "map": "village",
        "main_quest": 0,
        "side_quest_1": False,
        "side_quest_2": False
    })

    return True


def login(username, password):
    result = users.get(
        (User.username == username) &
        (User.password == password)
    )

    return result


def save_player(player):
    users.update(player.to_dict(),
                 User.username == player.username)