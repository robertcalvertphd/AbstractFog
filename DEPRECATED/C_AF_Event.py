# A series of interactions
from DEPRECATED.C_Interaction import  Interaction


class AF_Event:
    def __init__(self, interactions, event_functions, name = "default event name"):
        self.interactions = interactions
        self.event_functions = event_functions
        self.name = name

    def evaluate(self, function_id, **kwargs):
        status, returns = self.event_functions[function_id]( **kwargs)
        assert status is not False, "invalid event evaluation in" + self.name # for debug use only.
        return returns

    @staticmethod
    def poke_event_function(guyA, guyB):
        print(guyA.name + " pokes " + guyB.name)

        # DGK: DO you want to instantiate Interaction here, or at AF_Organization? I think the latter.
        str_agi_interaction = Interaction(Interaction.generic_strength_agility_interaction_function, guyA, guyB)

        str_agi_interaction.interact()
        #self.interactions[0].interact(guyA, guyB)

        return True, None
