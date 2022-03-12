"""rock paper scissors
By Bianca"""

from random import randint

print("\nRock Paper and Scissors")

option = int(input("Press 1 to play >> "))

while option == 1:

    person = int(input("\nWrite the number of your choice\n(1 Rock, 2 Paper, 3 Scissors) >> "))

    names = {1: "Rock", 2: "Paper", 3: "Scissors"}

    pc = randint(1, 3)  # ----- 1 is Rock, 2 is Paper, 3 is Scissors

    print("The pc choice is: ", names[pc], "\n\n", names[person], "VS", names[pc])

    if person == pc:
        print("Tie!")

    elif person == 1 and pc == 2 or person == 2 and pc == 3 or person == 3 and pc == 1:
        print("Lose")

    else:
        print("Win")

    option = int(input("Press 1 to play >> "))


