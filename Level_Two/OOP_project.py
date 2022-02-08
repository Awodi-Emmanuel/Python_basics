from random import shuffle
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
class Deck:
    # my_card = []
    # for s in SUITE:
    #     for r in RANKS:
    #         my_card.append((s,r))
    def __init__(self):
        print("Creating New Order Deck!")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]
    def shuffle(self):
        print("SHUFFLING DECK")  
        shuffle(self.allcards)
    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])      
class Hand:                       
    def __init__(seif,cards):
        self.cards = cards
    
    def __str__(self):        return "Contains {} cards".format(len(self.cards))    