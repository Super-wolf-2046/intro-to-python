import random
player= raw_input("Rock, Paper, or Scissors")
if player == computer:
    print("you have tied")
elif player == "Rock":
    if computer == "Scissors":
        print("player wins battle", player,"Crushes", computer)
elif player == "Paper":
    if computer == "Rock":
        print("computer lost", player, "Covers", computer)
elif player == "Scissors":
    if computer == "Paper":
        print("Player wins", player, "cuts", computer)
elif player == "Rock":
    if computer == "Paper":
        print("Computer won", computer, "covered",player)
elif player == "Paper":
    if computer == "Scissors":
        print("And the winner is computer", computer, "cuts", player)
elif player == "Scissors":
    if computer == "Rock":
        print("computer is the winner", computer, "crushed", player) 