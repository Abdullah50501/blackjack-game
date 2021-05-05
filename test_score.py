from CardClass import Deck
from CardClass import Player
import random

deck = Deck(5)
deck.shucards(4)
p = Player('abdullah', 1000)

d = 'a'
while d != 'q':
    p.addcards(deck.draw(random.randrange(1, 5)))
    p.phand()
    d = input('q to exit')
    p.addcards(clean=True)
