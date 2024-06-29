import random 

class Card:
    RANK_ORDER = {'6': 0, '7': 1, '8': 2, '9': 3, '10': 4, 'J': 5, 'Q': 6, 'K': 7, 'A': 8, 'Joker': 9}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def beats(self, other_card, trump_suit):
        if self.rank == 'Joker':
            return True
        if other_card.rank == 'Joker':
            return False
        if self.suit == trump_suit and other_card.suit != trump_suit:
            return True
        if self.suit != trump_suit and other_card.suit == trump_suit:
            return False
        if self.suit == other_card.suit:
            return Card.RANK_ORDER[self.rank] > Card.RANK_ORDER[other_card.rank]
        return False



class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
                      for suit in ['hearts', 'diamonds', 'clubs', 'spades']]
        self.cards += [Card('6', 'hearts'), Card('6', 'diamonds')]  
        self.cards += [Card('Joker', 'none'), Card('Joker', 'none')]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_hand(self):
        return [self.cards.pop() for _ in range(9)]

    def reset(self):
        self.__init__()
