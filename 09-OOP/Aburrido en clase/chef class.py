import random


class CulinaryOverlordAndCommanderOfTheSacredFlame:

    def __init__(self, name, specialty, mood=10, do_i_hate_my_life=False):
        self.do_i_hate_my_life = self.do_i_hate_my_life
        self.mood = mood
        self.name = name
        self.specialty = specialty

    def cök(self):
        if not self.do_i_hate_my_life:
            qualiteh = random.randint(1, 10) + self.mood
            return qualiteh
        else:
            qualiteh = random.randint(1, 10) + self.mood
            return qualiteh

    def judgy_judges(self, skillz):
        if skillz >= 18:
            self.mood += 5
            print("UwU... 👉👈")
        elif skillz in range(10, 18):
            self.mood += 2
            print("*minecraft villager noise*")
        elif skillz in range(5, 10):
            self.mood -= 2
            print("Nahh..")
        else:
            self.mood -= 5
            print("🤢🤢🤢")

    def weather(self):
        if self.mood >= 8:
            self.do_i_hate_my_life = False

        else:
            self.do_i_hate_my_life = True