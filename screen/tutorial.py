import arcade

import ttd.constants
from ttd.screen.game import GameScreen


class TutorialScreen:
    def __init__(self, main, width: int, height: int):
        self.width = width
        self.height = height

        self.main = main

        self.texts = [
            "Welcome to TTD! TTD is a game about\n"
            "treating as many patients as possible in your local clinic\n"
            f"Every day, you have enough resources to treat "
            f"{int(ttd.constants.BUDGET / ttd.constants.TREATMENT_COST)} patients\n"
            f"However, you have {ttd.constants.PATIENTS_PER_DAY} patients per day",

            f"You start with a budget of R{ttd.constants.BUDGET} per day",

            "There are 3 possible actions:\n"
            "Treat    --    Triage    --    Diagnose",

            f"Treating takes the biggest amount of money, R{ttd.constants.TREATMENT_COST}\n"
            f"Since you have R{ttd.constants.BUDGET}, you can treat "
            f"{int(ttd.constants.BUDGET / ttd.constants.TREATMENT_COST)} patients,\n"
            "assuming that you do not diagnose any patients",

            "Treating a patient will cure them of their ailments.\n"


            f"Diagnosing takes R{ttd.constants.DIAGNOSE_COST}. This is equivalent to\n"
            f"the price of treating {int(ttd.constants.TREATMENT_COST / ttd.constants.DIAGNOSE_COST)}, "
            "so diagnose carefully!",

            "Triaging is the act of choosing which order you will treat your patients.\n"
            "However, if you do not treat a patient soon enough, then they may die!",

            "You have been assigned by the Department of Health\n"
            "to a local clinic in the North-West Province. The situation is bad here,\n"
            f"so you can expect to get roughly {ttd.constants.PATIENTS_PER_DAY} patients per day. You can only treat\n"
            f"{int(ttd.constants.BUDGET / ttd.constants.TREATMENT_COST)} patients per day. Choose wisely!"
        ]

        self.text_index = 0
        self.text = arcade.create_text(self.texts[self.text_index], arcade.color.BLACK, 15,
                                       align="center", anchor_x="center", anchor_y="center")
        self.text_shown = 0

    def key_press(self, key: int, modifiers: int):
        pass

    def key_release(self, key: int, modifiers: int):

        if self.text_shown > 1:

            if self.text_index + 1 < len(self.texts):
                self.text_index += 1

                self.text = arcade.create_text(self.texts[self.text_index], arcade.color.BLACK, 15,
                                               align="center", anchor_x="center", anchor_y="center")

            else:
                self.main.game_screen = GameScreen(self.main, self.width, self.height)

    def update(self, dt: float):
        self.text_shown += dt

    def draw(self):

        arcade.start_render()

        arcade.render_text(self.text, self.width / 2, self.height / 2)
