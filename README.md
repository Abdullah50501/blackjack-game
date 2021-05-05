# blackjack-game
a simple blackjack game 

## blackjack version 1.0:
This is my first python project.  
ceated on May 4, 2021 by Abdullah @ Qurashi505051  
Feel free to contact me for any sugition   
It is a terminal blackjack game with one player with starting balance of 1000 and AI dealer.    

#### File description:
  1. Blackjack.py    --> is the main game code.
  2. CardClass.py    --> containe both Deck and Player classes.
  3. test_score      --> is a test code for the class method Player.score()
  4. balootCarddraw  --> is a logic for dealing cards in the game baloot. 
  5. remaing files are created by pycharm editor and included.
 
#### Classes description:
  1. Deck:  
      is a class to represnet any number of decks of cards it has below methods:  
        
        a. Deck.shucards() --------->   This function shuffles the deck argument decide how many times default is 1.  
        b. Deck.draw()      -------->   This function remove #cards from deck returns it as a list default is 1 card removed.  
                                        Removed card are from index -1 so the top of the deck is index -1 and last card is index 0.  
                                        Removed cards are collected in self.removedcards if it is needed after the fact.  
        c. Deck.redrawncard() ------>   return #cards from the removed pile to the deck.  
                                        note returned cards will be on the top of the deck "index -1".  
        d. Dexk.lenremainingcard()-->  return the # of card in the deck.  
    
  2. Player:  
       Is a class to his class represent player and dealer of blackjack player has a name, list of card 'hand', and money balance. it has below methods:  
         
        a. Player.hand()        --> This function only return the list of card with player.  
        b. Player.phand()       --> This function print player hand and score on terminal if dealer is true then first card will not be shown on terminal.  
        c. Player.addcards()    --> This function add list of card to the player hand if clean is True it will removed all cards from player hand.  
        d. Player.score()       --> This function calculate the score of the player based on his hand.  
