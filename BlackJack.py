import os
from CardClass import Player
from CardClass import Deck
from time import sleep


def show_table(sd=True):
    os.system('cls')
    print(p1.name, '\t\tBet Size  = ', bet, '\t\tMoney balance = ', p1.money),
    dd.phand(dealer=sd)
    p1.phand()


# Setting of the game
number_of_decks = 7
percentage_to_reshuffle = 0.3
minimum_cards_in_deck = 52 * number_of_decks * percentage_to_reshuffle
player_money = 1000
number_of_shuffles = 10

# Create a deck and get players name and create players
table_creating = True
os.system('cls')
deck = Deck(number_of_decks)
deck.shucards(number_of_shuffles)
dd = Player('Dealer', 0)
while table_creating:
    try:
        p1 = Player(input('What is your name?  '), player_money)
        table_creating = False
    except:
        print('Input must be a positive hole number')

# Start the Game
gameStatus = True
num_rounds = 0
while gameStatus:
    # clear terminal and welcome player and count round
    profit = p1.money - player_money
    if num_rounds == 0:
        pperr = 0
    else:
        pperr = profit/num_rounds
    num_rounds += 1
    os.system('cls')
    print('Let\' play ....')
    print(p1.name, '\t\tMoney balance = ', p1.money,'\t Profit: ', profit, '\t Round: ', num_rounds, '\t P/R: ', pperr)
    print('')

    # This loop take the bet from player
    betin = False
    bet = 0
    while not betin:
        bet = 0
        try:
            bet = int(input('how much do you want to bet ....'))
            if p1.money >= bet > 0:
                betin = True
                p1.money -= bet
                os.system('cls')
        except:
            print('amount should be a a positive number :)')

    # Deal first hand
    p1.addcards(deck.draw(1))
    dd.addcards(deck.draw(1))
    p1.addcards(deck.draw(1))
    dd.addcards(deck.draw(1))
    show_table()

    # check for blackjack
    blackjack = False
    if p1.score() == 21:
        blackjack = True

    # Take player action 'hit or stand' also check for bust
    else:
        player_action = input('\nEnter s to stand, h to hit ...')
        while p1.score() <= 21 and player_action == 'h':
            p1.addcards(deck.draw(1))
            show_table()
            if p1.score() <= 21:
                player_action = input('\nEnter s to stand, h to hit ...')
        show_table(False)

    # Dealer action
    sleep(1.4)
    dealer_not_ready = True
    while dealer_not_ready:
        if dd.score() <= 16:
            dd.addcards(deck.draw(1))
            show_table(False)
            sleep(1.4)
        else:
            dealer_not_ready = False

    # Who win the Game and money handling
    print('')
    print('-----------------------------------------')
    if blackjack:
        print('WOW BLACKJACK, you WIN .... :)')
        p1.money += (bet * 2.5)
    elif p1.score() > 21:
        print('you busted good luck next time :(')
    elif p1.score() == dd.score():
        print('Draw .....')
        p1.money += bet
    elif p1.score() > dd.score() or dd.score() > 21:
        print('you win .... :)')
        p1.money += (2 * bet)
    elif p1.score() < dd.score():
        print('you lose ... :(')
    else:
        print('ERORR .. please contact devolper ...')

    # play Againe or exit
    # check money balance and exit game as will
    if p1.money < 1 or input('q for Quit, any key to play again') == 'q':
        gameStatus = False
        os.system('cls')
        print('Good Game see you again....')
        print(p1.name, '\t\tMoney balance = ', p1.money, '\t Profit: ', profit, '\t Round: ', num_rounds, '\t P/R: ',
              pperr)
        print('')
    p1.addcards(clean=True)
    dd.addcards(clean=True)
    if deck.lenremainingcard() < percentage_to_reshuffle:
        deck = Deck(number_of_decks)
        deck.shucards(10)
