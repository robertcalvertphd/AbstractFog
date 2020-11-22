# A series of Events
from C_AF_Event import AF_Event
from C_Interaction import Interaction


class Organization:
    def __init__(self, governing_function, events = None, name = "default organization name"):
        # consider the use of events...
        self.events = events
        self.governing_function = governing_function
        self.name = name

    def run(self, **kwargs):
        status, returns = self.governing_function(**kwargs)
        assert status is not False, "invalidly run organization in" + self.name # for debug use only.
        return returns

    @staticmethod
    def choose_action(actor, possible_targets):
        #choice = input("POKE or other things that are not implemented")
        choice = "POKE"
        # knows actor and determines target
        # could create many interactions
        interactions = []
        if choice == "POKE":
            interactions.append(Interaction(Interaction.generic_strength_agility_interaction_function,actor,possible_targets[0]))
            event = AF_Event(interactions,[AF_Event.poke_event_function])
            event.evaluate(function_id=0, guyA=actor, guyB = possible_targets[0])
        ## continue logic

        return True, None

