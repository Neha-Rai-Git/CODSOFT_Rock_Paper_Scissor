import random

print("""
╔════════════════════════════╗
║ ROCK PAPER SCISSORS GAME   ║
╚════════════════════════════╝
""")

user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid Choice! Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("\n╔══════════════════╗")
        print("║   Match Draw!    ║")
        print("╚══════════════════╝")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):

        print("\n+-----------------------+")
        print("|       You Win!        |")
        print("+-----------------------+")
        user_score += 1

    else:
        print("\n+-----------------------+")
        print("|    Computer Wins!     |")
        print("+-----------------------+")
        computer_score += 1

    print("\n╔══════════════╗")
    print("║ Score Board  ║")
    print("╚══════════════╝")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nPlay again? (y/n): ").lower()

    if play_again == "y":
        continue

    elif play_again == "n":
        print("\n╔══════════════╗")
        print("║ Final Score  ║")
        print("╚══════════════╝")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)

        if user_score > computer_score:
            print("\n+--------------------------------+")
            print("| You are the Overall Winner! 🎉 |")
            print("+--------------------------------+")

        elif computer_score > user_score:
            print("\n+----------------------------------+")
            print("| Computer is the Overall Winner! |")
            print("+----------------------------------+")

        else:
            print("\n+------------------------+")
            print("|      Match Tied!       |")
            print("+------------------------+")

        break

    else:
        print("Please enter only 'y' or 'n'.")
