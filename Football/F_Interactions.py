import _CORE as c
from Football.F_ENUMS import E
import random as r


class I_Engage_defender(c.AF_Interaction):
    WHIFF = 0
    SORTA = 1
    SOLID = 2
    PERFECT = 3

    def __init__(self, blocker, defender):
        super().__init__(I_Engage_defender.engage_defender_function, blocker, defender, E.ENGAGE_DEFENDER)

    def engage_defender_function(self):
        self.result = r.randint(0, 3)
        print("BLOCK", self.actorA, self.actorB)
        return True


class I_Execute_block(c.AF_Interaction):
    WHIFF = 0
    SORTA = 1
    SOLID = 2
    PERFECT = 3

    def __init__(self, blocker, defender):
        super().__init__(I_Execute_block.block_function, blocker, defender, E.EXECUTE_BLOCK)

    def block_function(self):
        self.result = r.randint(0, 3)
        print("BLOCK", self.actorA, self.actorB)
        return True


class I_Engage_runner(c.AF_Interaction):
    WHIFF = 0
    SORTA = 1
    SOLID = 2
    PERFECT = 3

    def __init__(self, defender, runner):
        super().__init__(I_Engage_runner.block_function, defender, runner, E.ENGAGE_RUNNER)

    def block_function(self):
        self.result = r.randint(0, 3)
        print("enage_runner",self.actorA, self.actorB)
        return True


class I_Tackle_runner(c.AF_Interaction):
    WHIFF2 = 4
    SORTA2 = 5
    SOLID2 = 6
    PERFECT2 = 7

    def __init__(self, defender, runner):
        super().__init__(I_Tackle_runner.tackle_function, defender, runner, E.TACKLE_RUNNER)

    def tackle_function(self):
        self.result = r.randint(0, 3)
        print("Tackle", self.actorA, self.actorB)
        return True


