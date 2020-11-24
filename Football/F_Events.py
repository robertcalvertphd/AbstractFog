from _CORE import AF_Event
import Football.F_Interactions as I
from copy import deepcopy

class E_Tackle(AF_Event):

    def __init__(self, defensive_player, runner):

        self.engage_runner = I.I_Engage_runner(defensive_player, runner)
        self.tackle_runner = I.I_Tackle_runner(defensive_player, runner)
        super().__init__(E_Tackle.event_func, "Tackle Event")

    def event_func(self):
        results = []

        # Engage
        #status, result = self.engage_runner.interact()
        self.engage_runner.interact()
        result = self.engage_runner.result
        self.interactions.append(self.engage_runner)
        if result is I.I_Engage_runner.WHIFF:
            return True
        elif result is I.I_Engage_runner.SORTA:
            level1 = "TACKLE WITH MOD-"
            mod = -1
        elif result is I.I_Engage_runner.SOLID:
            level1 = "TACKLE WITH NO MOD"
            mod = 0
        elif result is I.I_Engage_runner.PERFECT:
            level1 = "TACKLE WITH MOD+"
            mod = 1
        else:
            assert False, "Bad result from I_Engage_runner"

        # Tackle
        status, result = self.tackle_runner(mod)
        self.interactions.append(self.tackle_runner)

        success = [I.I_Tackle_runner.SORTA, I.I_Tackle_runner.SOLID, I.I_Tackle_runner.PERFECT]
        if result is I.I_Tackle_runner.WHIFF:
            return True
        elif result in success:
            return True
        else:
            assert False, "Bad result from I_Tackle_runner"


class E_Block(AF_Event):

    def __init__(self, blocker, defender):

        self.engage_defender = I.I_Engage_defender(blocker, defender)
        self.execute_block = I.I_Execute_block(blocker, defender)
        super().__init__(E_Tackle.event_func, "Block Event")

    def event_func(self):
        results = []

        # Engage
        self.engage_defender.interact()
        self.interactions.append(self.engage_defender)
        result = self.engage_defender.result
        if result is I.I_Engage_defender.WHIFF:
            return True
        elif result is I.I_Engage_defender.SORTA:
            mod = -1
        elif result is I.I_Engage_defender.SOLID:
            mod = 0
        elif result is I.I_Engage_defender.PERFECT:
            mod = 1
        else:
            assert False, "Bad result from I_Engage_defender"

        # Block
        # TODO: Update mod on each block attempt.
        success = [I.I_Execute_block.SORTA, I.I_Execute_block.SOLID, I.I_Execute_block.PERFECT]


        self.execute_block(mod)
        result = self.execute_block.result
        self.interactions.append(deepcopy(self.execute_block))

        while result in success:

            self.execute_block(mod)
            result = self.execute_block.result
            self.interactions.append(deepcopy(result))

        if result is I.I_Execute_block.WHIFF:
            return True

        else:
            assert False, "Bad result from I_Execute_block"


class Silly:
    def __init__(self, value):
        self.value = value

class Example:
    ENUM_VALUE = 1
    DEFINED_CLASS = Silly(2)

    def __init__(self):
        self.instanced_class = Silly(3)

    def non_static_function(self):
        print("This is a instance level function", self.instanced_class.value)
        print("In the instance level function this is static", Example.DEFINED_CLASS.value)

    @staticmethod
    def static_function():
        print("In static level function", Example.DEFINED_CLASS.value)
        print("this function can not know about self.")


'''
e = Example()

e.non_static_function()
Example.static_function()
e.static_function()
'''
