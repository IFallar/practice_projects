import random

print("Rock, Paper, Scissors\n")

options = ["Rock", "Paper", "Scissors"]

Score = [0, 0]

PlayerScore = Score[0]
ComputerScore = Score[1]


while PlayerScore < 5 and ComputerScore < 5:

    x = (random.randint(0, 1))

    Computer = options[x]
    Player = input("\nRock, Paper or Scissors?\n")

    print(Player + " vs. " + Computer + "\n")

    if Player == Computer:
        print("Tie!")

    elif Player == "Rock":
        if Computer == "Paper":
            print(Computer + " wraps " + Player + "!")
            ComputerScore += 1
        elif Computer == "Scissors":
            print(Player + " smashes " + Computer + "!")
            PlayerScore += 1

    elif Player == "Paper":
        if Computer == "Scissors":
            print(Computer + " cuts " + Player + "!")
            ComputerScore += 1
        elif Computer == "Rock":
            print(Player + " wraps " + Computer + "!")
            PlayerScore += 1

    elif Player == "Scissors":
        if Computer == "Rock":
            print(Computer + " smashes " + Player + "!")
            ComputerScore += 1
        elif Computer == "Paper":
            print(Player + " cuts " + Computer + "!")
            PlayerScore += 1

    print("Player: " + str(PlayerScore) + "\n" + "Computer: " + str(
        ComputerScore))

if PlayerScore == 5:
    print("Player Wins!")
elif ComputerScore == 5:
    print("Computer Wins!")