class Skill:

    def __init__(self, name, cooldown):
        self.name = name
        self.cooldown = cooldown


class Slash(Skill):

    def __init__(self):
        super().__init__("Slash", 0)


class Fireball(Skill):

    def __init__(self):
        super().__init__("Fireball", 3)

    def use(self, monster):
        monster.hp -= 25


class Heal(Skill):

    def __init__(self):
        super().__init__("Heal", 4)

    def use(self, player):
        player.hp += 30

        if player.hp > player.max_hp:
            player.hp = player.max_hp


class PowerStrike(Skill):

    def __init__(self):
        super().__init__("Power Strike", 5)

    def use(self, monster):
        monster.hp -= 40