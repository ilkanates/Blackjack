- Player starts with 100 dollars in wallet
- Player decides on amount to bet, checked against the wallet
- Player gets 2 cards, 2 visible
- Dealer gets 2 cards, 1 visible, 1 hidden
- 
- WIN-LOSE CHECK: How much points does the deck has?
  - [=21] - WIN - END TURN
  - [>21] - LOSE - while >21 If the deck has A, count it as 1 instead of 11 - END TURN
  - [<21] - Continue
  
- ASK FOR MORE CARDS - Ask if player wants 1 more card
  - YES
    - Add card to player's deck
    - WIN-LOSE CHECK
  - NO 
    - DEALER'S TURN

- DEALER'S TURN
  - Show hand, 2 cards
  - Compare dealer's and player's total points
  - If dealer is losing: While total is < 16
    - Add card to dealer's deck
    - WIN-LOSE CHECK for dealer
    
- Compare dealer's and player's total points
  - END TURN

- END TURN
  - If player loses: deduct money from wallet
  - If player wins: add money to wallet
  - If wallet > 0
    - Ask for new turn
  - else
    - player loses - end game