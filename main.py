import random

# ASCII Art for Rock, Paper, Scissors
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

# List of weapons for easy management
weapons = [rock, paper, scissors]

def play_game():
    print("Let's play Rock, Paper, Scissors! Choose your weapon!")
    while True:
        try:
            x = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
            if x not in [0, 1, 2]:
                print("Invalid choice. Exiting the game. Thanks for playing!")
                break

            print(f"\nYou picked:\n{weapons[x]}")

            # Computer's choice
            c = random.randint(0, 2)
            print(f"The computer picked:\n{weapons[c]}")

            # Determine the result
            if x == c:
                print("It's a tie!\n")
            elif (x == 0 and c == 2) or (x == 1 and c == 0) or (x == 2 and c == 1):
                print("You win!\n")
            else:
                print("You lose!\n")

        except ValueError:
            print("Invalid input! Please type a number (0, 1, or 2).")

if __name__ == "__main__":
    play_game()
