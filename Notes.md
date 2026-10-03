# The general rules and logic behind the game no code :


## Bets :

- Players place their bets before the start of the game and before seeing the cards.

- The dealer in case of winning wins the players bets , and in case of losing match there bets and give them their earnings .


## Cards :
- Cards from 2 to 9 have there face value 
- Jacks , Queens , Kings have the value of 10 
- The Ace card can be have the value of 1 or 11 , and the player gets to choose between them through out the round.
- Deck of Cards 52.

## Rules : 

- The game start with the players placing there bets first , when bets are close the dealer deals one card to each player face up from a shuffled deck of cards then deals one to himself face up also. 

- After that he deals in the same order a second card to each player face up , then he deals a second  card for himself face down.

- If a player cards add up to 21 (a 10 value card with and ace) he wins immediately and wins  x1,5 his bet from the dealer its called *Black Jack*. if not and you want more cards to say *hit* and dealer give you an additional card (there is no limit to the number of cards you can add) but if it exceed 21 then it's a *bust* and the dealer gets your bet, and if you don't want any more cards you say *stand*. Also important note if you get 21 after a hit you don't win immediately you have to wait for the dealer to play.  

- Once this operation has gone around the table for each player then the dealer flip his face down card if it's 16 or under they have to take another card.if its 17 or higher they have to say with there hand.if the dealer bust every active player gits twice his bet.if he doesn't every player who has less value than the dealer loses his bet , if its the same then its a *push* and the player wins his bet,
and if he has value less than a player gets his bet . 

- If the dealer has a face up card Ace then the second one a 10 value card then its black jack and its a *push* for every player that doesn't have a blackjack.

- *Double Down* after you get your second card and its your turn to play you can double down meaning double your bet for one more hit or meaning one more card and then your turn ends and the normal rules apply. 

- *Split* if you get two similar cards in value you can split by them into two separate bets , the second bet has to match the first bet in value then the normal rules apply to each bet. 

- Insurance is not available in this version . 

- If the deck runs out of cards mid-round, shuffle the discard pile back into the deck and continue dealing.

-After each round ends, all cards from every hand (players and dealer) are moved into a discard pile. When the deck runs out of cards mid-round, the discard pile is shuffled and becomes the new deck.

- If a hand created from a split reaches 21, it still counts as Blackjack and pays 1.5x.

- Aces are split like any other pair.

-Re-splitting is not allowed, if you draw another matching pair on a split hand, you keep playing it as a normal hand.

-You can double down on a hand created from a split, following the normal double down rules.

## Player actions :
Hit: take another card
Stand: keep your current total, end your turn
Double down: double your bet, take exactly one more card, then automatically stand
Split: if your two cards have the same value, split them into two separate hands, each with its own bet


## Soft and Hard Hand

Soft hand: contains an Ace currently counted as 11.

Hard hand: either has no Ace, or the Ace(s) can only count as 1 without busting.

The dealer must stand on any 17, whether hard or soft.





# The coding logic and the structure : 

- Key elements from the game : **Dealer** **Player** **Hand** **Bets** **Deck** **Split Hand** **Discard pile**

All the following elements are  probably classes

## Deck : 
All cards from a 52 , colors : 26 red and 26 black , types : Diamond(♦),Spade(♠),Clubs(♣),Hearts(♥).

The Deck of cars must be able to be reshuffled randomly and deals from the top so the data structure must respect that , options : list , stack ??

All cards are a assigned a value for number cards the value = number , for King Queen Jack its 10 and for ace ist 1 or 11 

## Discard pile :

When the deck has no cards left to deal, the discard pile is shuffled and becomes the new deck. This can happen mid round if needed.

## Player :
Each player has a hand , bets and Actions : Hit , Stand , Double Down , Split 
And a starting pot meaning money to enter the game if the pot is equal to 0 player loses and GAME OVER

Game outcomes for a play : Bust , Push , Black jack , Normal Win, Loss these are methods   for the class Player

## Dealer : 
A Dealer has also a hand but first card face up second down , he needs to hit if below or equal 16 and stand if equals 17 or higher. 

Actions :
Deal,Reveal,Hit,Stand,Pay out , Collect , Return Bet , Reshuffle 

## Hand :

- Starts with two cards, except a Split Hand, which starts with one card (from the split pair) and is then dealt a second.
- Cards can be added according to the player's action (Hit adds cards without limit; Double Down adds exactly one card, then forces Stand).
- The hand's total must follow simple arithmetic addition of card values, and stays valid only while under or equal to 21.

### Ace value rule
- Each Ace is worth 11 unless that would push the total over 21 — in that case it's worth 1.
- Only one Ace per hand can ever count as 11 at a time. Any additional Aces in the same hand automatically count as 1, even if the total wouldn't otherwise bust.

### Soft vs Hard
- **Soft hand**: contains an Ace currently counted as 11.
- **Hard hand**: either has no Ace, or every Ace in the hand is counted as 1 (because counting any as 11 would bust).

## Split hand :
Created when the player's original cards are identical and also if they choose to