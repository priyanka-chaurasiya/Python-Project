import random

print("===== ROCK PAPER SCISSORS GAME =====")

choices = ["rock", "paper", "scissors"]

while True:
    # User choice
    user = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # Computer choice
    computer = random.choice(choices)

    print("You chose      :", user)
    print("Computer chose :", computer)

    # Determine winner
    if user == computer:
        print("Result: It's a Tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("🎉 You Win!")

    else:
        print("💻 Computer Wins!")

    # Play again
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break