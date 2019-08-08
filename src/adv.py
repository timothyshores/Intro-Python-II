import sys
from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("outside")
player2 = Player(Room("outside"))

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# print(chr(27) + "[2J")

currently_playing = True

room_name = room[repr(player1)].name
room_description = room[repr(player1)].description

print(room_name)
print(room_description)

while currently_playing:
    current_room = f'{player1}'

    print(f"\nCurrent room: {room[current_room].name}")
    print(f"Description: {room[current_room].description}\n")

    user_action = input(
        "Enter a direction \n - n for north, \n - e for east, \n - s for south and \n - w for west \n - q to quit: ").lower()

    direction = ['']

    if user_action == 'q':
        print('Thanks for playing')
        sys.exit(1)
    else:
        print('You did not press q')
