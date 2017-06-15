import arcade
import numpy
from typing import Set
from typing import Tuple
import random

import assets.assets
import constants


class PatientsGui:
    def __init__(self, screen, width: int, height: int):

        self.width = width
        self.height = height
        self.screen = screen

        self.patient_index = 0
        self.patients = PatientsGui.generate_patients(15)
        self.patients_order = []
        self.current_patient_text = None
        self.cur_gui = "triaging"

        # DAY gui
        self.day = 1
        self.shown_day = 0
        self.day_text = arcade.create_text(f"Day {self.day}", arcade.color.BLACK, 20,
                                           align="center", anchor_x="center", anchor_y="center")

    @staticmethod
    def generate_patient():

        symptoms = set()

        while len(symptoms) != 3:

            symptom = numpy.random.choice([sympt for sympt, p, imp in constants.SYMPTOMS],
                                          p=[p for sympt, p, imp in constants.SYMPTOMS])

            symptoms.add(constants.SYMPTOMS[constants.SYMPTOMS_INDEXES[symptom]])

        return Patient(symptoms)

    @staticmethod
    def generate_patients(n):

        return [PatientsGui.generate_patient() for _ in range(n)]

    @property
    def patients_text(self):

        string = "Patients:\n"
        num = 0

        for patient in self.patients_order:

            num += 1
            string += f"{num}. {patient.name}: {patient.survival_chance}% survival\n"

        return arcade.create_text(string, arcade.color.BLACK)

    @property
    def patients_deaths(self):

        string = "Patients: \n"

        for patient in self.patients:

            string += "{0}: {1}\n".format(patient.name, "dead" if patient.dead else "alive")

        return arcade.create_text(string, arcade.color.BLACK, 20,
                                  align="center", anchor_x="center", anchor_y="center")

    def key_press(self, key: int, modifier: int):

        if self.cur_gui == "triaging":
            if key in range(48, 58):

                if len(self.patients_order) < 10 and self.patients[self.patient_index] not in self.patients_order:
                    self.patients_order.insert(key - 48, self.patients[self.patient_index])

                if self.patient_index < len(self.patients) - 1:
                    self.patient_index += 1

                else:
                    self.simulate()
                    self.day += 1
                    self.cur_gui = "death"

        if key == arcade.key.SPACE:

            if self.cur_gui == "triaging":
                if self.patient_index < len(self.patients) - 1:
                    self.patient_index += 1

                else:
                    self.simulate()
                    self.day += 1
                    self.cur_gui = "death"

            else:
                self.cur_gui = "day"
                self.day += 1

    def key_release(self, key: int, modifiers: int):
        pass

    def simulate(self):

        for patient in self.patients:

            hospital_bonus = 35 - self.patients_order.index(patient) * 5 if patient in self.patients_order else 0
            survival_chance = patient.survival_chance + hospital_bonus
            survive = random.randint(1, 100)

            if survive > survival_chance:
                patient.dead = True

    def update(self, dt: float):

        if self.cur_gui == "day":
            if self.shown_day < 1:
                self.shown_day += dt

            else:
                self.cur_gui = "triaging"
                self.patient_index = 0
                self.patients = PatientsGui.generate_patients(15)
                self.patients_order = []
                self.current_patient_text = None

    def draw(self):

        if self.cur_gui == "triaging":
            patient = self.patients[self.patient_index]

            patient_text = arcade.create_text(
                                              f"Name: {patient.name}\n"
                                              "Symptoms:\n"
                                              f"{list(patient.symptoms)[0][0]}\n"
                                              f"{list(patient.symptoms)[1][0]}\n"
                                              f"{list(patient.symptoms)[2][0]}\n"
                                              f"Survival chance: {patient.survival_chance}",
                                              arcade.color.BLACK, 20,
                                              align="center", anchor_x="center", anchor_y="center")

            arcade.draw_text("Press the number you want to have this patient treated (0 INDEXED)",
                             10, 10, arcade.color.BLACK)

            arcade.render_text(patient_text, self.width / 2 + 100, self.height / 2)
            arcade.draw_texture_rectangle(self.width / 2 - 50, self.height / 2, 100, 100, patient.texture)
            arcade.render_text(self.patients_text, 10, self.height - 10)

        elif self.cur_gui == "death":
            arcade.render_text(self.patients_deaths, self.width / 2, self.height / 2)

        elif self.cur_gui == "day":
            self.day_text = arcade.create_text(f"Day {self.day}", arcade.color.BLACK, 20,
                                               align="center", anchor_x="center", anchor_y="center")
            arcade.render_text(self.day_text, self.width / 2, self.height / 2)



class Patient:

    def __init__(self, symptoms: Set[Tuple[str, int]] = ()):

        self.symptoms = symptoms
        self.gender = random.choice(("male", "female"))
        self.dead = False

        # GENERATED USING listofrandomnames.com
        self.name = random.choice([
            "Adolfo",
            "Mitch",
            "Warren",
            "Chance",
            "Jonas",
            "Titus",
            "Arron",
            "Chase",
            "Owen",
            "Ariel"
        ]) if self.gender == "male" else random.choice([
            "Lashawna",
            "Mui",
            "Janice",
            "Kiesha",
            "Kathaleen",
            "Soo",
            "Lissette",
            "Georgiana",
            "Odette",
            "Olga"
        ])

        self.texture = random.choice(assets.assets.MALE) \
            if self.gender == "male" else random.choice(assets.assets.FEMALE)

    @property
    def survival_chance(self):

        return 100 - sum([sympt[2] for sympt in self.symptoms])
