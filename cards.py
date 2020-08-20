import random
class Card():
    """     The Card class represents a single playing card and is initialised by passing a suit and number.
    """

    def __init__(self, suit, number):
        """ This is a default constructor used to initialise instance variables or attributes for Card object """
        self._suit = suit
        self._number = number
        

    def __repr__(self):

        """This method is used to represent a output in better manner or understandable form """
        return (self._number + " of " + self._suit)   
    
    @property
    def suit(self):
        """This method is used to get the suit value(as getter method)"""
        return self._suit

    @suit.setter
    def suit(self,suit):
        """This method is used to set the values to suit variable (like setter method) """
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit.upper()    

        else:
            print("This is not a suit")    

    @property
    def number(self):
        """ This method is used to get values of number variable """
        return self._number

    @number.setter
    def number(self,number):
        """ This method is used to set values for number variable """
        if number in [str(i) for i in range(2,11)] + ['J', 'Q', 'K', 'A']:
            self._number = number    


class Deck():
    """ The Deck class represents a list of total 52 playing cards 
        The Deck class represents a deck of playing cards in order. 
    """

    def __init__(self):

        """ This is a default constructor used to initialise instance variables or attributes for Deck object """


        self._cards = []
        self.populate()
        print(self._cards)


    def populate(self):
        """ This method is used to populate the deck of cards with all 52 cards in the order 2-10, J,Q,K,A, hearts, clubs, diamonds, spades"""
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)]+["J", "Q", "K", "A"]
         
        self._cards = [ Card(s,n) for s in suits for n in numbers ]

    def shuffle(self):

        """ Shuffle the deck into a random order of playing cards """
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """ Deals(and removes) a number of cards from the deck 
            Returns : list of Card objects
        """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
        
deck = Deck()
print(deck)    

