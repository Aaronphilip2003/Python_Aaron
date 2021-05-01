import random

comp=random.randint(1,3)

player=0

player_turn=input("Enter Rock,Paper or Scissors:")

player_lower=player_turn.lower()

# Converting player turns to numbers for ease of if-else blocks

if player_lower == "rock":
    player=1
elif player_lower == "paper":
    player=2
elif player_lower == "scissors":
    player=3

# Rock=1
# Paper=2
# Scissors=3


if player==1:
    if comp==1:
        print("TIE! The computer chose Rock")
    elif comp==2:
        print("You Lost! The computer chose Paper")
    elif comp==3:
        print("You Won! The computer chose Scissors")

if player==2:
    if comp==1:
        print("You Won! The computer chose Rock")
    elif comp==2:
        print("Tie! The computer chose Paper")
    elif comp==3:
        print("You Lost! The computer chose Scissors")

if player==3:
    if comp==1:
        print("You Lost! The computer chose Rock")
    elif comp==2:
        print("You Won! The computer chose Paper")
    elif comp==3:
        print("TIE! The computer chose Scissors")








