# Represents an intellectual ability
class Ability:
    # A percentage level of the ability, where 1 matches human level
    level = 0

    # The name of the ability
    name = ""

    # A description of the ability
    description = ""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def improve(self):
        # Implement the logic to improve this ability
        pass

    def assess(self):
        # Implement the logic to assess this ability
        pass

    def get_level(self):
        return self.level

# A specific ability
class Ability1(Ability):
    def __init__(self):
        super().__init__("Ability 1", "This is the first ability")

# Another specific ability
class Ability2(Ability):
    def __init__(self):
        super().__init__("Ability 2", "This is the second ability")


class Agent:
    def __init__(self):
        # An agent will have many abilities.
        # Note: the the number of abilities is finite.
        self.ability1 = Ability1()
        self.ability2 = Ability2()