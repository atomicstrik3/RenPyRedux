init python:
    import core

label start:

    "Hello, buddy."

    scene expression core.get_background("player_room")
    $ core.main()

    return

screen test():
    tag menu

    frame:
        has vbox
        text "Time of Day: [core.get_time_of_day()]"

    frame:
        align(0.5, 0.5)
        has vbox

        text "This is the Game Loop!" size 40
        textbutton "Advance Time":
            action Function(lambda: (core.advance_time(), core.update("player_room")) )