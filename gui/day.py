import arcade


class DayGui:
    def __init__(self, screen, width: int, height: int):

        self.width = width
        self.height = height
        self.screen = screen

        self.day = 1
        self.shown_day = 0
        self.day_text = arcade.create_text(f"Day {self.day}", arcade.color.BLACK, 20,
                                           align="center", anchor_x="center", anchor_y="center")

    def update(self, dt: float):

        if self.shown_day < 1:
            self.shown_day += dt

        else:
            # self.screen.gui = GuiScreen.PATIENTS  # TODO
            pass

    def draw(self):

        arcade.render_text(self.day_text, self.width / 2, self.height / 2)
