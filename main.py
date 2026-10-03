import random


#First creating the classes for the key elements in a game of BlackJack


#Creating Card class 

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit} "


#Creating Deck class 

class Deck:
    

    def __init__(self):
        self.deck = []
        self.discard = []
        self.Suits = ["Diamonds","Spades","Clubs","Hearts"]
        self.Rank = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        self.build()
        self.shuffle()

    #this function serve to build a 52 card deck
    def build(self):
        for i in self.Suits:
            for j in self.Rank:
                self.deck.append(Card(i,j))

    #randomly shuffle a deck of cards as per the casino/game rules
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if self.deck != [] :
            return self.deck.pop()
            



#Creating the Hand Class

class Hand:
    rank_points = {
        "Ace" : 11,
        'Two' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5,
        'Six' : 6,
        'Seven' : 7,
        'Eight' : 8,
        'Nine' : 9 ,
        'Ten' : 10 ,
        'Jack' : 10 ,
        'Queen' : 10,
        'King' : 10 
    }


    def __init__(self):
        self.hand = []


    def total_value(self):
        total = 0 
        ace_count = 0 
        for card in self.hand:
            total += self.rank_points[card.rank]
            if card.rank == 'Ace':
                ace_count += 1 
        while  total > 21 and ace_count >= 1 :
            total -= 10 
            ace_count -= 1 
        return total

    def add_card(self,card):
        self.hand.append(card)

    def is_bust(self):
        return self.total_value() > 21 

    def is_blackjack(self):
        return self.total_value() == 21 and len(self.hand) == 2 
        


#Creating the Player class 

class Player:


    def __init__(self,bet):
        self.bet = bet 
        self.hand = Hand()
        self.done = False
        self.earnings = 0


    def hit(self,card):
        self.hand.add_card(card)

    def stand(self):
        self.done = True

    def double_down(self,card):
        self.bet = self.bet * 2 
        self.hit(card)
        self.done = True 

#Creating the dealer class :

class Dealer:

    def __init__(self):
        self.hand = Hand()

    def play(self,deck):
        while self.hand.total_value() <= 16 :
            self.hand.add_card(deck.deal())

# Simulating a round 

Game_Deck = Deck()
Game_Dealer = Dealer()
Player1 = Player(1000)
Player2 = Player(2000)
Player3 = Player(3000)

Players = [Player1,Player2,Player3]


def play_round(players,dealer,deck):
    
    for player in players:
        player.hand.add_card(deck.deal())
    
    dealer.hand.add_card(deck.deal())

    for player in players:
        player.hand.add_card(deck.deal())
    dealer.hand.add_card(deck.deal())

    for player in players :
        if dealer.hand.is_blackjack() :
            if player.hand.is_blackjack() :
               player.earnings += player.bet * 1.5 
               player.done = True
        else :
            if player.hand.is_blackjack() :
                player.earnings += player.bet * 1.5 
                player.done = True 

    if not players[0].done :
        players[0].hit(deck.deal())
        players[0].stand()

    
    if not players[1].done :
        players[1].double_down(deck.deal())

    if not players[2].done : 
        players[2].hit(deck.deal())
        players[2].hit(deck.deal())
        players[2].stand()

    dealer.play(deck)   

    if not dealer.hand.is_bust() :
        for player in players:
            if not player.hand.is_bust() and not player.hand.is_blackjack():
                if player.hand.total_value() > dealer.hand.total_value():
                    player.earnings += player.bet

                elif  player.hand.total_value() == dealer.hand.total_value() :
                    pass
                
                else :
                    player.earnings -= player.bet

            else :
                if player.hand.is_bust():
                    player.earnings -= player.bet
    else : 
        for player in players : 
            if not player.hand.is_bust() and not player.hand.is_blackjack():
               player.earnings += player.bet

            elif player.hand.is_bust():
                player.earnings -= player.bet
            



play_round(Players, Game_Dealer, Game_Deck)

for player in Players:
    print(f"Hand total: {player.hand.total_value()}, Bust: {player.hand.is_bust()}, Bet: {player.bet}, Earnings: {player.earnings}")

print(f"Dealer total: {Game_Dealer.hand.total_value()}, Bust: {Game_Dealer.hand.is_bust()}")


for player in Players:
    print([str(card) for card in player.hand.hand])

print([str(card) for card in Game_Dealer.hand.hand])