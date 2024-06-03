rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

while True:
    print("Lets play Rock, Paper,  Scissors! Choose your weapon!")
    x = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    c = random.randint(0, 2)
    if x != 0 and x != 1 and x != 2:
        print("Thanks for playing! Goodbye!")
        break
    if x == 0:
        print("You picked Rock!")
        print(rock)
        if c == 0:
            print("And I picked Rock!")
            print(rock)
            print("Its a tie!\n \n \n")
        elif c == 1:
            print("And I picked Paper!")
            print(paper)
            print("You lose!\n \n \n")
        else:
            print("And I picked Scissors!")
            print(scissors)
            print("You win!\n \n \n")
    elif x == 1:
        print("You picked Paper!")
        print(paper)
        if c == 0:
            print("And I picked Rock!")
            print(rock)
            print("You win!\n \n \n")
        elif c == 1:
            print("And I picked paper!")
            print(paper)
            print("Its a tie!\n \n \n")
        else:
            print("And I picked Scissors!")
            print(scissors)
            print("You lose!\n \n \n")
    else:
        print("You picked Scissors!")
        print(scissors)
        if c == 0:
            print("And I picked Rock!")
            print(rock)
            print("You lose!\n \n \n")
        elif c == 1:
            print("And I picked paper!")
            print(paper)
            print("You win!\n \n \n")
        else:
            print("And I picked Scissors!")
            print(scissors)
            print("Its a tie!\n \n \n")
