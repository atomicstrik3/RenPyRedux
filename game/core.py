time_states = ["morning", "day", "evening", "night"]
current_index = 0

def main():
    """Hide UI and Dialogue Box"""
    import renpy.exports as renpy
    import store    # This is where _window_hide() function lives

    """Hide Window"""
    renpy.hide_screen("say")
    store._window_hide()

    """Call the Test Screen"""
    renpy.show_screen("test")

    """Freeze the Screen"""
    while True:
        renpy.pause(1.0, hard=True)

def get_time_of_day():
    return time_states[current_index]

def advance_time():
    global current_index
    current_index = (current_index + 1) % len(time_states)

def get_background(location):
    """ Return image background """
    return f"Backgrounds/{location}/{get_time_of_day()}.png"

def update(location):
    import renpy.exports as renpy
    from renpy.display.image import Image

    path = get_background(location)
    renpy.scene()   #Clears the screen
    renpy.show("bg_dynamic", what=Image(path), tag="master")