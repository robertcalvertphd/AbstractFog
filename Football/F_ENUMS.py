class E:


    INVALID_INTERACTION = False, None

    #TYPES
    ATTRIBUTE = 1000
    INTERACTION = 1100
    ORGANIZATION = 1200
    #...


    STRENGTH = ATTRIBUTE + 0
    AGILITY = ATTRIBUTE + 1
    ENDURANCE = ATTRIBUTE + 2

    # INTERACTION TYPES
    ENGAGE_DEFENDER = INTERACTION + 0
    EXECUTE_BLOCK = INTERACTION + 1
    ENGAGE_RUNNER = INTERACTION + 2
    TACKLE_RUNNER = INTERACTION + 3

    # ORGANIZATION TYPES
    RUN_PLAY = ORGANIZATION + 0

    @staticmethod
    def E2str(id):
        if      id == E.INVALID_INTERACTION:    return "Invalid Interaction"
        elif    id == E.STRENGTH:               return "Strength"
        elif    id == E.AGILITY:                return "Agility"
        elif    id == E.ENDURANCE:              return "Endurance"
        elif    id == E.ENGAGE_DEFENDER:        return "Engage Defender"
        elif    id == E.EXECUTE_BLOCK:          return "Execute Block"
        elif    id == E.ENGAGE_RUNNER:          return "Engage Runner"
        elif    id == E.TACKLE_RUNNER:          return "Tackle Runner"
        elif    id == E.RUN_PLAY:               return "Run Play"
        else:   assert False, "E2str: Invalid Enum id " + str(id)