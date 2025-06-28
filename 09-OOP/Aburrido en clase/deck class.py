import random

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
        self.cards = [(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num = 1):
        wagwan = self.cards[:num]
        self.cards = self.cards[num:]
        return wagwan

    def whaslef(self):
        return f"There's {len(self.cards)} left in the deck. "