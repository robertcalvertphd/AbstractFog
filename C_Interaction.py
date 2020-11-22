# a collection of attribute comparisons
from ENUMS import E
from C_Actor import Actor
from C_AF_Attribute import AF_Attribute as Attribute

class Interaction:
    def __init__(self, interaction_function, actorA, actorB, name = "default interaction name"):
        self.actorA = actorA
        self.actorB = actorB
        self.governing_function = interaction_function
        self.name = name

    def interact(self, **kwargs):
        status, returns = self.governing_function(self.actorA, self.actorB, **kwargs)
        assert status is not False, "invalid interaction in" + self.name # for debug use only.
        return returns

    @staticmethod
    def generic_strength_agility_interaction_function(attacker, defender):
        print("there was an interaction between ", attacker.name, " and ", defender.name)
        return True, None

'''
def example_compete1(x):
    print("example1:", x)


def example_compete2(x,y):
    print("example2:",x,y)


def interaction_function(actorA, actorB):
    return True, actorA.attributes[0].values[0]


a = Attribute([2],[example_compete1, example_compete2])

#a.enact(0,x=a.value)
#a.enact(1,x=a.value, y = 4)

p1 = Actor([a])
p2 = Actor([a])

# example interaction

i = Interaction(interaction_function,p1,p2,"BOB")
j = i.interact()
print(j)
'''