from random import shuffle
import unittest


class Card:
    """
    Create a card of a deck
    """
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]
    """What suit has the card?"""

    values = ["2", "3", "4",
              "5", "6", "7",
              "8", "9", "10",
              "Ace", "Jack",
              "Queen", "King"]
    """What value has the card?"""

    def __init__(self, v, s):
        """
        Determine what is the value and the suit of card
        :param v: value of card
        :param s: suit of card
        """
        self.value = v
        self.suit = s

    def __repr__(self):
        """
        create printable representation
        :return: string that represents a card (Ex: 2 of ace)
        """
        v = self.values[self.value] + \
            " of " + \
            self.suits[self.suit]
        return v

    def get_value(self):
        """
        return value of card
        :return: integer that represents value of card
        """
        return self.value + 2

    def rank(self):
        """
        determine rank of card to be sorted
        :return: integer that represents rank of card
        """
        if self.value < 9:
            return self.value + 2
        elif self.value == 9:
            return 11
        elif self.value == 10:
            return 12
        elif self.value == 11:
            return 13
        else:
            return 14


class Deck:
    """
    create a deck with 52 cards
    """
    def __init__(self):
        """
        create a list with 52 cards
        """
        self.cards = []
        for i in range(0, 13):
            for j in range(4):
                self.cards.append(Card(i, j))

    def rm_card(self):
        """
        remove card from deck
        :return: card that was removed
        """
        if len(self.cards) == 0:
            return
        return self.cards.pop()

    def shuffle_deck(self):
        """
        shuffle deck
        :return: None
        """
        shuffle(self.cards)

    def player_hand(self):
        """
        draw 2 cards for player
        :return: tuple consisting of 2 cards or None if deck doesn't have 2 cards
        """
        if len(self.cards) == 1:
            return
        return self.cards.pop(), self.cards.pop()

    def table_hand(self):
        """
        draw 5 cards for table
        :return: tuple consisting of 5 cards or None if deck doesn't have 5 cards
        """
        if len(self.cards) == 4:
            return
        return self.cards.pop(), self.cards.pop(), self.cards.pop(), self.cards.pop(), self.cards.pop()

    def sort_cards(self):
        """
        sort deck
        :return: None
        """
        def sort_key(card):
            """
            key for sorting cards
            :param card: Card
            :return: rank of card
            """
            return card.rank()
        self.cards = sorted(self.cards, key=sort_key)

    def list_of_cards(self):
        """
        give a list that represents the deck
        :return: list with cards

        """
        return self.cards


class CardTest(unittest.TestCase):
    def test_sort_cards(self):
        deck = Deck()
        deck.shuffle_deck()
        deck.sort_cards()
        res = deck.list_of_cards()
        list_res = []
        for i in res:
            list_res.append(i.get_value())
        self.assertEqual(list_res, [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
                                    7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12,
                                    13, 13, 13, 13, 14, 14, 14, 14])

    def test_player_hand(self):
        deck = Deck()
        res = deck.player_hand()
        self.assertEqual(len(res), 2)

    def test_table_hand(self):
        deck = Deck()
        res = deck.table_hand()
        self.assertEqual(len(res), 5)

