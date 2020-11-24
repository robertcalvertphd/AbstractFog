


class AF_Actor:
    def __init__(self, attributes, information = {"DEFAULT":"DEFAULT_INFORMATION"}, id = None):
        self.attributes = attributes
        self._id = id
        self.information = information


class AF_Attribute:
    def __init__(self, values, action_functions, id = None):
        self.action_functions = action_functions
        self.values = values
        self._id = id

    def enact(self, function_id, **kwargs):
        return self.action_functions[function_id](self,**kwargs)


class AF_Interaction:
    def __init__(self, interaction_function, actorA, actorB, id = None):
        self.actorA = actorA
        self.actorB = actorB
        self.governing_function = interaction_function
        self._id = id
        self.result = None

    def interact(self, **kwargs):
        status = self.governing_function(self, **kwargs)
        assert status is not False, "AF_Interaction: invalid interaction. World-specific id=" + str(self._id) # for debug use only.
        return status


class AF_Event:
    # events are vertical with potential branches off. They inherently deal with 2 actors over some number of ticks.
    # The result of an event is an array of completed Interactions that are fully parameterized
    def __init__(self, event_function, id = None):
        self.interactions = []      # To be populated by event_function with completed result, with dynamic member count
        self.event_function = event_function
        self._id = id

    def evaluate(self, **kwargs):
        status = self.event_function(self, **kwargs)
        assert status is not False, "AF_Event: invalid event evaluation in event. World-specific id=" + str(self._id)   # for debug use only.
        return status


class AF_Organization:
    def __init__(self, governing_function, id = None):
        # consider the use of events...
        self.events = []
        self.governing_function = governing_function
        self._id = id

    def run(self, **kwargs):
        status = self.governing_function(**kwargs)
        assert status is not False, "AF_Organization: unlawful organization with id=" + str(self._id) # for debug use only.
        return status
