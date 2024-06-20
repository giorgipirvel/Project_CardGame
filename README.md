# Final_Project

# Short OverView:

The project was done in Python. It's about the card game - Joker, game is played by four people. Program is receiving player names and then randomly give us the order which determines the first dealer and player who is choosing the trump. The game consists of 4 Fours and in each Four, there are 4 plays, overall we have 16 plays. After each Four, program shows score distribution among players and in the end, prints who is the winner of the game according to accumulated points.


# Main Concepts

- Dealer: The player who deals the cards in current round
- Four: 4 plays give us Four
- Word: Each player's prediction on how many cards he can take before each play
- Fulfillment of the word: If player said that he would take x cards and actually picked up x cards.
- Penalty: If player's word is non-zero and failed to pick at least one card, he is fined by 500 points
- Score: Each word and picked number of cards corresponds to some score( see below ) 
- Trump: Trump is chosen by the first player of the play according to initial 3 cards
- Cutting card: Defeating a card, the cards belong to player who has highest value card


# Rules

- Program randomly deals 9-9 cards to each player
- In Each play players choose trump from 3 initial cards
- Players indicate their words based on 9 cards
- Round starts and finished after all cards were being played
- Using proper suits is crucial
- Not having same suit means that you should use trump or joker
- Not having neither means that you can use any card
- In same suits, wins one with the highest value
- Trump can defeat nontrump cards
- Trump can be defeated by another higher value trump and Joker
- Joker defeats all the cards, can be defeated by another Joker only

# Order of cards - From lowest to highest value
```
  ┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐     ┌───────┐    
  |6      |     |7      |     |8      |     |9      |     |10     |     |J      |     |Q      |     |K      |     |A      |     |JOK    |    
  |  ♥ ♠  | ==> |  ♥ ♠  | ==> |  ♥ ♠  | ==> |  ♥ ♠  | ==> |  ♥ ♠  | ==> |  ♥ ♠  | ==> |  ♥ ♠  | ==> |  ♥ ♠  | ==> |  ♥ ♠  | ==> |  ♥ ♠  |
  |  ♣ ♦  |     |  ♣ ♦  |     |  ♣ ♦  |     |  ♣ ♦  |     |  ♣ ♦  |     |  ♣ ♦  |     |  ♣ ♦  |     |  ♣ ♦  |     |  ♣ ♦  |     |  ♣ ♦  |  
  |      6|     |      7|     |      8|     |      9|     |     10|     |      J|     |      Q|     |      K|     |      A|     |    JOK|
  └───────┘     └───────┘     └───────┘     └───────┘     └───────┘     └───────┘     └───────┘     └───────┘     └───────┘     └───────┘
  
```

# Score distribution table
```
                   T   A   K   E   N
                      
    |   0   |  1  |  2   |  3   |  4  |  5  |  6  |  7  |  8  |  9
____|_______|_____|______|______|_____|_____|_____|_____|_____|______
0   |  50   | 10  |  20  |  30  |  40 |  50 |  60 |  70    80 |  90         
1   | -500  | 100 |  20  |  30  |  40 |  50 |  60 |  70 |  80 |  90         
2   | -500  | 10  |  150 |  30  |  40 |  50 |  60 |  70 |  80 |  90         W
3   | -500  | 10  |  20  |  200 |  40 |  50 |  60 |  70 |  80 |  90         
4   | -500  | 10  |  20  |  30  | 250 |  50 |  60 |  70 |  80 |  90         O   
5   | -500  | 10  |  20  |  30  |  40 | 300 |  60 |  70 |  80 |  90
6   | -500  | 10  |  20  |  30  |  40 |  50 | 350 |  70 |  80 |  90         R
7   | -500  | 10  |  20  |  30  |  40 |  50 |  60 | 400 |  80 |  90
8   | -500  | 10  |  20  |  30  |  40 |  50 |  60 |  70 | 450 |  90         D
9   | -500  | 10  |  20  |  30  |  40 |  50 |  60 |  70 |  80 | 900

```
