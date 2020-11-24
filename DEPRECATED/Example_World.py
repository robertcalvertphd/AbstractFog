import random as r

from DEPRECATED.C_Actor import Actor
from DEPRECATED.C_Organization import Organization
from DEPRECATED.C_AF_Attribute import AF_Attribute


# defines attribute functions
# defines other rules that make this no longer generic

# units live here and no where else


def basic_check(value):
    ret = 0
    for i in range(value):
        ret+= r.randint(1,6)
    return ret


def create_guy(name):
    strength = AF_Attribute(1,basic_check)
    agility = AF_Attribute(1,basic_check)
    awareness = AF_Attribute(1,basic_check)
    guy = Actor(attributes=[strength,agility,awareness],name=name)
    return guy









abe = create_guy("ABE")
bob = create_guy("BOB")
cal = create_guy("CAL")


fight = Organization(Organization.choose_action)
fight.run(actor = abe, possible_targets = [bob,cal])

print("Concluded")
