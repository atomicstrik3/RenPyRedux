init python:
    import core

label start:

    "Hello, buddy."

    $ core.main()

    return

screen test():
    tag menu

    frame:
        align(0.5, 0.5)
        has vbox

        text "This is the Game Loop!" size 40