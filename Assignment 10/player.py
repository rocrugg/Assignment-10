class Player:

    def __init__(self, data):
        self.username = data["username"]
        self.level = data["level"]
        self.xp = data["xp"]
        self.gold = data["gold"]
        self.hp = data["hp"]
        self.max_hp = data["max_hp"]
        self.inventory = data["inventory"]
        self.skills = data["skills"]
        self.map = data["map"]
        self.main_quest = data["main_quest"]

    def gain_xp(self, amount):
        self.xp += amount

        if self.xp >= self.level * 100:
            self.level += 1
            self.max_hp += 20
            self.hp = self.max_hp

            print("LEVEL UP!")

    def to_dict(self):
        return {
            "username": self.username,
            "level": self.level,
            "xp": self.xp,
            "gold": self.gold,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "inventory": self.inventory,
            "skills": self.skills,
            "map": self.map,
            "main_quest": self.main_quest
        }