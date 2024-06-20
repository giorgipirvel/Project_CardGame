from score import calculate_score

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.word = 0
        self.round_wins = 0
        self.score = 0

    def show_initial_cards(self):
        print(f"\n{self.name}'s initial cards: {[(card.rank, card.suit) for card in self.hand[:3]]}")

    def choose_trump(self):
        while True:
            try:
                index = int(input(f"{self.name}, choose a trump card by index (0-2): "))
                if 0 <= index <= 2:
                    return self.hand[index].suit
            except (ValueError, IndexError):
                print("Please choose a valid index (0, 1, or 2).")

    def choose_word(self, exclude=None):
        while True:
            word = int(input(f"{self.name}, enter your word (0-9): "))
            if 0 <= word <= 9 and (exclude is None or word != exclude):
                self.word = word
                return word

    def play_card(self, played_cards, trump_suit):
        lead_card = played_cards[0] if played_cards else None
        lead_suit = lead_card.suit if lead_card and lead_card.rank != 'Joker' else None
        while True:
            print(f"\n{self.name}'s hand: {[(card.rank, card.suit) for card in self.hand]}")
            try:
                index = int(input(f"{self.name}, play a card by index: "))
                if 0 <= index < len(self.hand):
                    chosen_card = self.hand[index]
                    if self.can_play_card(chosen_card, lead_suit, trump_suit):
                        return self.hand.pop(index)
                    else:
                        if lead_suit:
                            print(f"You must follow the lead suit ({lead_suit}) if you have same suit card")
                        if not self.has_suit(lead_suit) and self.has_suit(trump_suit):
                            print(f"You must play a trump card ({trump_suit})")
            except (ValueError, IndexError):
                print("Please choose a valid index.")

    def can_play_card(self, card, lead_suit, trump_suit):
        if card.rank == 'Joker':
            return True 
        if not lead_suit:
            return True  
        if card.suit == lead_suit:
            return True  
        if card.suit == trump_suit:
            return not any(c.suit == lead_suit for c in self.hand)  
        return not any(c.suit == lead_suit or c.suit == trump_suit for c in self.hand)  

    def has_suit(self, suit):
        return any(card.suit == suit for card in self.hand)

    def add_round_win(self):
        self.round_wins += 1

    def calculate_score(self):
        self.score += calculate_score(self.word, self.round_wins)
        self.round_wins = 0
