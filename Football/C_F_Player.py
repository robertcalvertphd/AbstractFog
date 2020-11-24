import _CORE as c

from Football.C_F_Attribute import F_Attribute as att


class C_Player(c.AF_Actor):
    def __init__(self):

        strength = att([1],att.basic_check, "STRENGTH")
        agility =  att([1],att.basic_check, "AGILITY")
        endurance =  att([1],att.basic_check,"ENDURANCE")
        attributes = [strength, agility, endurance]
        super().__init__(attributes=attributes)

    def attack(self, opponent):
        i = c.AF_Interaction(example_interaction, self, opponent, "attack")
        return i


def example_interaction(attacker, defender):
    print(attacker.name, " attacks ", defender.name)
    return True, True



