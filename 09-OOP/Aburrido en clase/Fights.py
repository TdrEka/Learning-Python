import random

class Animal:
    def __init__(self, name, strength, dexterity, constitution):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution

    def calculate_defense(self):
        base_defense = (self.dexterity + self.constitution) / 2

        random_modifier = random.randint(-int(base_defense * 0.3), int(base_defense * 0.3))
        return max(0, base_defense + random_modifier)

    def damage_calc(self, strength):
        return strength - self.calculate_defense()

    def ouchie(self, attack_value):
        if self.damage_calc(attack_value) <= 0:
            return
        else: self.constitution -= self.damage_calc(attack_value)

    def atac(self, other_animal):
        if not self.ded_check():
            random_attack = self.strength + random.randint(-self.strength // 2, self.strength // 2)
            other_animal.ouchie(random_attack)

    def ded_check(self):
        return self.constitution <= 0

    def shotgun(self):
        return max(0, random.randint(0, self.dexterity))


tiger = Animal("Tony", 35, 10, 40)
bear = Animal("Bruno", 38, 8, 45)
tarrasque = Animal("Terry", 120, 5, 200)
cat = Animal("Mr. Whiskers", 20, 20, 8)
snail = Animal("Gary", 1, 1, 5)
platypus = Animal("Perry", 20, 15, 20)


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

fight_to_death(cat, platypus)