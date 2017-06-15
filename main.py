"""
TTD - ~~Time Till Death~~ Treat Triage Diagnose

Game made in 5h for CAT exam

Info in README

"""

import time

import arcade

from screen.start import StartScreen


class Game(arcade.Window):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)

        self.last_frame = time.time()
        self.update_accumulator = 0

        self.game_screen = StartScreen(self, width, height)

    def on_draw(self):
        dt = time.time() - self.last_frame
        self.last_frame = time.time()
        self.update_accumulator += dt

        if self.update_accumulator > 0.05:
            self.game_screen.update(self.update_accumulator)
            self.update_accumulator = 0.0

        self.game_screen.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        self.game_screen.key_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        self.game_screen.key_release(symbol, modifiers)


window = Game(640, 480)
time.sleep(1)  # Wait for screen to open

arcade.set_window(window)
arcade.run()
