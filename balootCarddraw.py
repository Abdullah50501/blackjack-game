from CardClass import Deck

deck = Deck(baloot=True)
d = 'a'
while d != 'q':
    deck.shucards(3)
    hand1 = deck.draw(3)
    hand2 = deck.draw(3)
    hand3 = deck.draw(3)
    hand4 = deck.draw(3)
    hand1 += deck.draw(2)
    hand2 += deck.draw(2)
    hand3 += deck.draw(2)
    hand4 += deck.draw(2)
    souq = deck.draw(1)
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)
    print(souq)
    input('hi')
    hand1.append(souq[0])
    souq = []
    hand1 += deck.draw(2)
    hand2 += deck.draw(3)
    hand3 += deck.draw(3)
    hand4 += deck.draw(3)
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)
    deck.print()
    d = input('hi')
    deck.redrawncard(32)