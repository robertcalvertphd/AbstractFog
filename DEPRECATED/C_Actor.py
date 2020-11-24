#   can compete
#   has attributes


class Actor:
    def __init__(self, attributes, information = {"DEFAULT":"DEFAULT_INFORMATION"}, name = "unnamed actor"):
        self.attributes = attributes
        self.name = name
        self.information = information