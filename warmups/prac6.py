class Monster:
    def __init__(self, name, number_of_teeth, colour):
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour = colour

    def __str__(self):

    def __int__(self):
        return str(vars(self))

    def is_scary(self):
        """Return True if the monster is scary, False otherwise."""
        if self.number_of_teeth > 20 or self.colour.lower() in ["black", "red", "dark green"]:
            return True
        else:
            return False