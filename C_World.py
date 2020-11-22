import random as r

from C_Actor import Actor
from C_Organization import Organization
from C_AF_Attribute import AF_Attribute
from C_AF_Event import AF_Event
from C_Interaction import Interaction
import ENUMS as E

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
