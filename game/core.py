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