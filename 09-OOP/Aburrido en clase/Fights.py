import random

class AnimalDeadError(Exception):
    pass

class Animal:
    def __init__(self, name, strength, dexterity, constitution):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.level = 1
        self.exp = 0
        self.exp_to_level = 10

    def calculate_defense(self):
        base_defense = (self.dexterity + self.constitution) / 2

        random_modifier = random.randint(-int(base_defense * 0.3), int(base_defense * 0.3))
        return max(0, base_defense + random_modifier)

    def damage_calc(self, strength):
        return max(0, strength - self.calculate_defense())

    def ouchie(self, attack_value):
        if self.damage_calc(attack_value) <= 0:
            return
        else: self.constitution -= self.damage_calc(attack_value)

    def atac(self, other_animal):
        if self.ded_check():
            raise AnimalDeadError(f"{self.name} is already dead, you monster!")
        if not self.ded_check():
            random_attack = self.strength + random.randint(-self.strength // 2, self.strength // 2)
            other_animal.ouchie(random_attack)

            if other_animal.ded_check():
                earned = other_animal.exp_to_award()
                self.gain_exp(earned)

    def exp_to_award(self):
        return max(1, (self.strength + self.dexterity + self.constitution) / 30)

    def ded_check(self):
        return self.constitution <= 0

    def shotgun(self):
        return max(0, random.randint(0, self.dexterity))

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} gains {round(amount, 2)} XP! ({round(self.exp, 2)}/{self.exp_to_level})")

        while self.exp >= self.exp_to_level:
            self.exp -= self.exp_to_level
            self.level_up()

    def level_up(self):
        self.level += 1
        self.strength += self.strength / 10
        self.dexterity += self.dexterity / 10
        self.constitution += self.constitution / 10
        self.exp_to_level = int(self.exp_to_level * 1.5)
        print(f"BRRRRR {self.name} just levelled up to level {self.level}!")

class Gastropod(Animal):
    def __init__(self, name, strength, dexterity, constitution):
        super().__init__(name, strength, dexterity, constitution)
        self.in_shell = False
        self.poison_stacks = {}

    def slime_trail(self, other):
        print(f"{self.name} leaves a sticky icky slime trail of dubious origin on {other.name}!")
        other.dexterity = max(0, other.dexterity -random.randint(1, 20))

    def cower_in_calcium_carbonate(self):
        print(f"{self.name} retreats into their shell and doomscrolls!")
        self.in_shell = True

    def toxic_slime(self, other):
        print(f"{self.name} secretes highly toxic mucus!")
        if other.name not in self.poison_stacks:
            self.poison_stacks[other.name] = 0
        self.poison_stacks[other.name] += 3
        other.constitution -= self.poison_stacks[other.name]
        print(f"{other.name} takes {self.poison_stacks[other.name]} poison damage!")

    def atac(self, other_animal):
        if self.ded_check():
            raise AnimalDeadError(f"{self.name} is already dead, you monster!")

        action = random.choice(['normal', 'slime', 'cower', 'toxic'])

        if action == 'normal':
            super().atac(other_animal)
        elif action == 'slime':
            self.slime_trail(other_animal)
        elif action == 'toxic':
            self.toxic_slime(other_animal)
        else:
            self.cower_in_calcium_carbonate()

    def ouchie(self, attack_value):
        if self.in_shell:
            print(f"{self.name}'s shell takes a part of the beating!")
            attack_value = max(1, attack_value  // random.randint(2, 10))
        super().ouchie(attack_value)
        self.in_shell = False

def fight_to_death(animal1, animal2):

    print(f"{animal1.name} vs {animal2.name} - FIGHT!")

    turn = 1
    while not animal1.ded_check() and not animal2.ded_check():
        print(f"\n--- Turn {turn} ---")

        speed1 = animal1.shotgun()
        speed2 = animal2.shotgun()

        if speed1 >= speed2:
            first, second = animal1, animal2
        else:
            first, second = animal2, animal1

        # Animal 1 attacks
        print(f"{first.name} attacks {second.name}!")
        first.atac(second)
        print(f"{second.name} health: {second.constitution}")

        if second.ded_check():
            print(f"{second.name} is DEAD! {first.name} wins!")
            break

        # Animal 2 attacks back
        print(f"{second.name} attacks {first.name}!")
        second.atac(first)
        print(f"{first.name} health: {first.constitution}")

        if first.ded_check():
            print(f"{first.name} is DEAD! {second.name} wins!")
            break

        turn += 1

tiger = Animal("Tony", 35, 10, 40)
bear = Animal("Bruno", 38, 8, 45)
tarrasque = Animal("Terry", 120, 5, 200)
cat = Animal("Mr. Whiskers", 20, 20, 8)
snail = Gastropod("Gary", 1, 1, 5)
platypus = Animal("Perry", 20, 15, 20)


fight_to_death(tiger, cat)