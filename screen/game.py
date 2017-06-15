import arcade

from ttd.gui.day import DayGui


class GameScreen:
    def __init__(self, main, width: int, height: int):
        self.width = width
        self.height = height

        self.main = main

        # General
        self.gui = DayGui(self, width, height)

        # PATIENTS gui screen
        self.patient_index = 0
        self.patients = []

        arcade.set_background_color(arcade.color.AERO_BLUE)

    def key_press(self, key: int, modifiers: int):
        pass

    def key_release(self, key: int, modifiers: int):
        pass

    def update(self, dt: float):
        self.gui.update(dt)

    def draw(self):
        arcade.start_render()

        self.gui.draw()
