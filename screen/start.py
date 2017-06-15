import arcade

from screen.tutorial import TutorialScreen


class StartScreen:
    def __init__(self, main, width: int, height: int):
        self.width = width
        self.height = height

        self.main = main

        self.timer = 2

        self.start_text = arcade.create_text("Press any key to start", arcade.color.BLACK, 20,
                                             align="center", anchor_x="center", anchor_y="center")

        arcade.set_background_color(arcade.color.AERO_BLUE)

    def key_press(self, key: int, modifiers: int):
        if self.timer < 2:
            self.main.game_screen = TutorialScreen(self.main, self.width, self.height)

    def key_release(self, key: int, modifiers: int):
        pass

    def update(self, dt: float):
        self.timer -= dt

    def draw(self):
        arcade.start_render()

        arcade.render_text(self.start_text, self.width / 2, self.height / 2)
