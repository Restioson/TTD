import arcade

from gui.patients import PatientsGui


class GameScreen:

    def __init__(self, main, width: int, height: int):
        self.width = width
        self.height = height

        self.main = main

        # General
        self.gui = PatientsGui(self, width, height)

        # PATIENTS gui screen
        self.patient_index = 0
        self.patients = []

        arcade.set_background_color(arcade.color.AERO_BLUE)

    def key_press(self, key: int, modifiers: int):
        self.gui.key_press(key, modifiers)

    def key_release(self, key: int, modifiers: int):
        self.gui.key_release(key, modifiers)

    def update(self, dt: float):
        self.gui.update(dt)

    def draw(self):
        arcade.start_render()

        self.gui.draw()
