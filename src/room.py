# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'Current Room: {self.name}, \nDescription: {self.description}'

    def __repr__(self):
        return f'Room: {repr(self.name)}, \nDescription: {repr(self.description)}'

    def name(self):
        return self.name

    def description(self):
        return self.description

    def north(self):
        if (self.name == 'Outside Cave Entrance'):
            self.name = "Foyer"
            self.description = "Dim light filters in from the south. Dusty passages run north and east."
        else:
            print("Unable to move north")
