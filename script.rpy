# The script of the game goes in this file.

init python:
    import re
    from texthandlercomplete import *

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    #Call checkFullText on the section of dialogue
    $ displayList = checkFullText("According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Yellow, black.", 180)

    #display the first element of the resulting list, and then pop it off, until the list is empty.
    while displayList:
        e "[displayList[0]]"
        $ displayList.pop(0)

    e "Wow, we split that text!"

    # This ends the game.

    return
