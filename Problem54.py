"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from random import randint


class Hand:
    hand_strength_tiers = {"Royal Flush": 10,
                           "Straight Flush": 9,
                           "Four of a Kind": 8,
                           "Full House": 7,
                           "Flush": 6,
                           "Straight": 5,
                           "Three of a Kind": 4,
                           "Two Pair": 3,
                           "Pair": 2,
                           "High Card": 1}

    def __init__(self, cards):
        self.cards = cards
        self.cards.sort()
        self.cards.reverse()

    def __repr__(self):
        return str(self.cards)

    def high_card(self):
        return self.cards[0]

    def is_flush(self):
        suits = [card.get_suit() for card in self.cards]
        return all(s == suits[0] for s in suits)

    def is_straight(self):
        numerical_values = [card.get_numerical_value() for card in self.cards]
        theoretical_straight = range(numerical_values[0], numerical_values[0] - len(numerical_values), -1)
        return numerical_values == list(theoretical_straight)

    def counts(self):
        values = [card.get_value() for card in self.cards]
        return {card.get_value(): values.count(card.get_value()) for card in self.cards}

    def quick_hand(self):
        if self.is_flush() and self.is_straight() and self.high_card().get_value() == "A":
            return "Royal Flush"
        elif self.is_flush() and self.is_straight():
            return "Straight Flush"
        elif 4 in self.counts().values():
            return "Four of a Kind"
        elif 3 in self.counts().values() and 2 in self.counts().values():
            return "Full House"
        elif self.is_flush():
            return "Flush"
        elif self.is_straight():
            return "Straight"
        elif 3 in self.counts().values():
            return "Three of a Kind"
        elif list(self.counts().values()).count(2) == 2:
            return "Two Pair"
        elif 2 in self.counts().values():
            return "Pair"
        else:
            return "High Card"

    @staticmethod
    def compare_cascades(casc1, casc2):
        for i in range(len(casc1)):
            if casc1[i] != casc2[i] and type(casc1[i]) is Card:
                return casc2[i].get_numerical_value() - casc1[i].get_numerical_value()
            elif casc1[i] != casc2[i]:
                return Deck.values[casc2[i]] - Deck.values[casc1[i]]
        return 0

    def compare(self, other):
        self_quick_hand_val = self.hand_strength_tiers[self.quick_hand()]
        other_quick_hand_val = other.hand_strength_tiers[other.quick_hand()]
        self_counts = self.counts()
        other_counts = other.counts()
        if self_quick_hand_val == other_quick_hand_val:
            if self_quick_hand_val == self.hand_strength_tiers["Royal Flush"]:
                # automatic tie
                return 0
            elif self_quick_hand_val == self.hand_strength_tiers["Straight Flush"]:
                # check high card
                return other.high_card().get_numerical_value() - self.high_card().get_numerical_value()
            elif self_quick_hand_val == self.hand_strength_tiers["Four of a Kind"]:
                # check front runner then compare cascade
                self_front_runner = [i for i, j in self_counts.items() if j == 4][0]
                self_cascade = [i for i, j in self_counts.items() if j != 4]
                other_front_runner = [i for i, j in other_counts.items() if j == 4][0]
                other_cascade = [i for i, j in other_counts.items() if j != 4]
                if self_front_runner == other_front_runner:
                    return Hand.compare_cascades(self_cascade, other_cascade)
                else:
                    return Deck.values[other_front_runner] - Deck.values[self_front_runner]
            elif self_quick_hand_val == self.hand_strength_tiers["Full House"]:
                self_front_runner_1 = [i for i, j in self_counts.items() if j == 3][0]
                self_front_runner_2 = [i for i, j in self_counts.items() if j == 2][0]
                other_front_runner_1 = [i for i, j in other_counts.items() if j == 3][0]
                other_front_runner_2 = [i for i, j in other_counts.items() if j == 2][0]

                # compare triples
                if self_front_runner_1 != other_front_runner_1:
                    return Deck.values[other_front_runner_1] - Deck.values[self_front_runner_1]
                else:
                    # else compare pair
                    return Deck.values[other_front_runner_2] - Deck.values[self_front_runner_2]
            elif self_quick_hand_val == self.hand_strength_tiers["Flush"]:
                return Hand.compare_cascades(self.cards, other.cards)
            elif self_quick_hand_val == self.hand_strength_tiers["Straight"]:
                return other.high_card().get_numerical_value() - self.high_card().get_numerical_value()
            elif self_quick_hand_val == self.hand_strength_tiers["Three of a Kind"]:
                # check front runner then compare cascade
                self_front_runner = [i for i, j in self_counts.items() if j == 3][0]
                self_cascade = [i for i, j in self_counts.items() if j != 3]
                other_front_runner = [i for i, j in other_counts.items() if j == 3][0]
                other_cascade = [i for i, j in other_counts.items() if j != 3]
                if self_front_runner == other_front_runner:
                    return Hand.compare_cascades(self_cascade, other_cascade)
                else:
                    return Deck.values[other_front_runner] - Deck.values[self_front_runner]
            elif self_quick_hand_val == self.hand_strength_tiers["Two Pair"]:
                self_list = [i for i, j in self_counts.items() if j == 2]
                self_list.sort()
                other_list = [i for i, j in other_counts.items() if j == 2]
                other_list.sort()
                self_front_runner_1 = self_list[0]
                self_front_runner_2 = self_list[1]
                other_front_runner_1 = other_list[0]
                other_front_runner_2 = other_list[1]

                # compare first pair
                if self_front_runner_1 != other_front_runner_1:
                    return Deck.values[other_front_runner_1] - Deck.values[self_front_runner_1]
                else:
                    # else compare pair
                    return Deck.values[other_front_runner_2] - Deck.values[self_front_runner_2]
            elif self_quick_hand_val == self.hand_strength_tiers["Pair"]:
                # check front runner then compare cascade
                self_front_runner = [i for i, j in self_counts.items() if j == 2][0]
                self_cascade = [i for i, j in self_counts.items() if j != 2]
                other_front_runner = [i for i, j in other_counts.items() if j == 2][0]
                other_cascade = [i for i, j in other_counts.items() if j != 2]
                if self_front_runner == other_front_runner:
                    return Hand.compare_cascades(self_cascade, other_cascade)
                else:
                    return Deck.values[other_front_runner] - Deck.values[self_front_runner]
            elif self_quick_hand_val == self.hand_strength_tiers["High Card"]:
                return Hand.compare_cascades(self.cards, other.cards)
        else:
            return other_quick_hand_val - self_quick_hand_val



class Deck:
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
              "J": 11, "Q": 12, "K": 13, "A": 14}
    suits = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}

    def __init__(self):
        self.cards = []
        for suit in self.suits.keys():
            for value in self.values.keys():
                self.cards.append(Card(value, suit))

    def draw_hand(self, size):
        drawn_cards = []
        for _ in range(size):
            rand_index = randint(0, len(self.cards) - 1)
            drawn_cards.append(self.cards[rand_index])
            self.cards.remove(self.cards[rand_index])
        return Hand(drawn_cards)


class Card:

    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
              "J": 11, "Q": 12, "K": 13, "A": 14}
    suits = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}

    def __init__(self, value, suit):
        if value == "T":
            self.value = '10'
        else:
            self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_numerical_value(self):
        return self.values[self.value]

    def get_suit(self):
        return self.suit

    def __eq__(self, other):
        return self.get_numerical_value() == other.get_numerical_value()

    def __lt__(self, other):
        return self.get_numerical_value() < other.get_numerical_value()

    def __le__(self, other):
        return self.get_numerical_value() <= other.get_numerical_value()

    def __repr__(self):
        return f"{self.value}{self.suits[self.suit]}"

player1_wins = 0
with open('p054_poker.txt') as hands_file:
    line = hands_file.readline()
    while line:
        line = line.rstrip()
        cards = line.split(' ')
        card_objects = [Card(card[0], card[1]) for card in cards]
        hand1 = Hand(card_objects[:5])
        hand2 = Hand(card_objects[5:])
        print(f'{hand1} -- {hand1.quick_hand()}')
        print(f'{hand2} -- {hand2.quick_hand()}')
        comp_value = hand1.compare(hand2)
        if comp_value < 0:
            print("Hand 1 wins")
            player1_wins += 1
        elif comp_value == 0:
            print("Tie")
        elif comp_value > 0:
            print("Hand 2 wins")
        line = hands_file.readline()

print(f'Player 1 won {player1_wins} hands')
