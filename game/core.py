class Game:

    def __init__(self):
        self.time_states = ["morning", "day", "evening", "night"]
        self.time_index = 0
        self.day = 1
        self.location = "player_room"
    
    def main(self):
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

    def get_time(self):
        return self.time_states[self.time_index]
    
    def advance_time(self):
        self.time_index = (self.time_index + 1) % len(self.time_states)
        if self.time_index == 0:
            self.day += 1

    def get_background(self):
        """ Return image background """
        return f"Backgrounds/{self.location}/{self.get_time()}.png"
    
    def update_scene(self):
        import renpy.exports as renpy
        from renpy.display.image import Image

        renpy.scene()   #Clears the screen
        renpy.show("bg_dynamic", what=Image(self.get_background()), tag="master")

game = Game()