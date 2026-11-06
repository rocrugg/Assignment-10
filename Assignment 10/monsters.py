class Monster:

    def __init__(self, name, hp, attack, gold):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.gold = gold


class Goblin(Monster):

    def __init__(self):
        super().__init__("Goblin", 30, 5, 15)


class Wolf(Monster):

    def __init__(self):
        super().__init__("Wolf", 40, 8, 20)


class Skeleton(Monster):

    def __init__(self):
        super().__init__("Skeleton", 50, 10, 30)


class Orc(Monster):

    def __init__(self):
        super().__init__("Orc", 70, 15, 50)


class Dragon(Monster):

    def __init__(self):
        super().__init__("Dragon", 120, 25, 100)


class FinalBoss(Monster):

    def __init__(self):
        super().__init__("Malzor", 200, 35, 500)