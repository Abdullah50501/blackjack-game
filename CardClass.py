import random


# This Class represent a deck of cards
# It can be 1 or multiple decks argument dictate how many decks default is 1
# If baloot is true it will be only one 32 cards deck missing following cards from all suits '2,3,4,5,6"
class Deck:

    def __init__(self, decks=1, baloot=False):
        self.NumberOfDecks = decks
        if baloot:
            self.cards = [
                '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', 'A of Hearts',
                '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', 'A of Spades',
                '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', 'A of Clubs',
                '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds', 'A of Diamonds',
            ]
        else:
            self.cards = self.NumberOfDecks * [
                '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', 'A of Hearts',
                '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', 'A of Spades',
                '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', 'A of Clubs',
                '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds', 'Q of Diamonds', 'K of Diamonds', 'A of Diamonds',
            ]

        self.removedcards = []      # to keep track of removed cards from deck if it is needed to be put in again

    # This function shuffles the deck argument decide how many times default is 1
    def shucards(self, numberofshuffle=1):
        for time in range(0, numberofshuffle):
            random.shuffle(self.cards)

    # This function remove #cards from deck returns it as a list default is 1 card removed
    # removed card are from index -1 so ..
    # The top of the deck is index -1 and last card is index 0
    # Removed cards are collected in self.removedcards if it is needed after the fact
    def draw(self, numberofcards=1):
        if len(self.cards) < numberofcards:
            return None
        hand = []
        for n in range(0, numberofcards):
            card = self.cards.pop()
            self.removedcards.append(card)
            hand.append(card)

        return hand

    # return #cards from the removed pile to the deck
    # note returned cards will be on the top of the deck "index -1"
    def redrawncard(self, numberofcards=1):

        for n in range(0, numberofcards):
            if len(self.removedcards) == 0:
                return None
            self.cards.append(self.removedcards.pop())

    # return the # of card in the deck
    def lenremainingcard(self):
        return len(self.cards)


# This class represent player and dealer of blackjack
# player has a name, list of card 'hand', and money balance
class Player:

    def __init__(self, PlayerName, player_money):
        self.name = PlayerName
        self.hand = []
        self.money = player_money

    # This function only return the list of card with player
    def hand(self):
        return self.hand

    # This function print player hand and score on terminal
    # If dealer is true then first card will not be shown on terminal
    def phand(self, dealer=False):
        if dealer:
            show = self.hand.copy()
            show[0] = 'Face Down Card'
            print(self.name, 'Hand:|', ', '.join(show), '|\t score is unknown ')
        else:
            print(self.name, 'Hand:|', ', '.join(self.hand), '|\t score is {} '.format(self.score()))

    # This function add list of card to the player hand
    # If clean is True it will removed all cards from player hand
    def addcards(self, cards=[], clean=False):
        if clean:
            re = self.hand
            self.hand = []
            return re
        else:
            self.hand += cards

    # This function calculate the score of the player based on his hand
    def score(self):
        score = 0
        a_count = 0
        for card in self.hand:
            if card[0] in ('J', 'Q', 'K') or card[1] == '0':
                score += 10
            elif card[0] == 'A':
                while True:
                    if score < 11:
                        score += 11
                        a_count += 1
                        break
                    elif a_count > 0:
                        score -= 10
                        a_count -= 1
                    else:
                        score += 1
                        break
            else:
                score += int(card[0])

        while score > 21 and a_count > 0:
            if score > 21 and a_count > 0:
                score -= 10
                a_count -=1

        return score

