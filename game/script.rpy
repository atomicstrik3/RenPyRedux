init python:
    import core
    from core import game

label start:

    "Hello, buddy."

    scene expression game.get_background()
    $ game.main()

    return

screen test():
    tag menu

    frame:
        has vbox
        text "Time of Day: [game.get_time()]"
        text "Time Index: [game.time_index]"
        text "Day: [game.day]"

    frame:
        align(0.5, 0.5)
        has vbox

        text "This is the Game Loop!" size 40
        textbutton "Advance Time":
            action Function(lambda: (game.advance_time(), game.update_scene()) )