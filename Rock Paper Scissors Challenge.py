# ==========================================================
#              ROCK PAPER SCISSORS GAME
# ==========================================================
# Technology: Python
# Features:
# 1. User vs Computer
# 2. Random computer choice
# 3. Multiple rounds
# 4. Score tracking
# 5. Winner declaration
# 6. Input validation
# 7. Play again option
# ==========================================================

import random


# ----------------------------------------------------------
# FUNCTION 1: Display Game Rules
# ----------------------------------------------------------

def show_rules():
    print("\n")
    print("=" * 60)
    print("              ROCK PAPER SCISSORS")
    print("=" * 60)

    print("\nGAME RULES:")
    print("1. Rock beats Scissors")
    print("2. Scissors beats Paper")
    print("3. Paper beats Rock")
    print("4. Same choice means Draw")

    print("\nChoices:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")


# ----------------------------------------------------------
# FUNCTION 2: Get User Choice
# ----------------------------------------------------------

def get_user_choice():

    while True:

        print("\nChoose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "Rock"

        elif choice == "2":
            return "Paper"

        elif choice == "3":
            return "Scissors"

        else:
            print("\nInvalid choice!")
            print("Please enter 1, 2, or 3.")


# ----------------------------------------------------------
# FUNCTION 3: Generate Computer Choice
# ----------------------------------------------------------

def get_computer_choice():

    choices = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(choices)

    return computer_choice


# ----------------------------------------------------------
# FUNCTION 4: Decide Winner
# ----------------------------------------------------------

def find_winner(user_choice, computer_choice):

    # If both choices are same
    if user_choice == computer_choice:
        return "Draw"

    # User winning conditions
    elif user_choice == "Rock" and computer_choice == "Scissors":
        return "User"

    elif user_choice == "Paper" and computer_choice == "Rock":
        return "User"

    elif user_choice == "Scissors" and computer_choice == "Paper":
        return "User"

    # Otherwise computer wins
    else:
        return "Computer"


# ----------------------------------------------------------
# FUNCTION 5: Display Round Result
# ----------------------------------------------------------

def display_round_result(user_choice, computer_choice, winner):

    print("\n")
    print("-" * 50)
    print("                ROUND RESULT")
    print("-" * 50)

    print("Your choice     :", user_choice)
    print("Computer choice :", computer_choice)

    if winner == "Draw":
        print("Result          : It's a Draw!")

    elif winner == "User":
        print("Result          : You Win!")

    else:
        print("Result          : Computer Wins!")

    print("-" * 50)


# ----------------------------------------------------------
# FUNCTION 6: Display Score
# ----------------------------------------------------------

def display_score(user_score, computer_score, draw_score):

    print("\n")
    print("=" * 50)
    print("                  SCORE")
    print("=" * 50)

    print("Your Score      :", user_score)
    print("Computer Score  :", computer_score)
    print("Draws           :", draw_score)

    print("=" * 50)


# ----------------------------------------------------------
# FUNCTION 7: Display Final Winner
# ----------------------------------------------------------

def display_final_winner(user_score, computer_score):

    print("\n")
    print("=" * 60)
    print("                 FINAL RESULT")
    print("=" * 60)

    print("Your Final Score     :", user_score)
    print("Computer Final Score :", computer_score)

    print("\n")

    if user_score > computer_score:

        print("🎉 CONGRATULATIONS!")
        print("You are the overall winner!")

    elif computer_score > user_score:

        print("Computer is the overall winner!")

    else:

        print("The game is tied!")
        print("Both players have the same score.")

    print("=" * 60)


# ----------------------------------------------------------
# FUNCTION 8: Play Game
# ----------------------------------------------------------

def play_game():

    user_score = 0
    computer_score = 0
    draw_score = 0

    # Ask number of rounds
    while True:

        try:

            rounds = int(input("\nEnter number of rounds: "))

            if rounds > 0:
                break

            else:
                print("Please enter a number greater than 0.")

        except ValueError:

            print("Please enter a valid number.")


    # ------------------------------------------------------
    # GAME LOOP
    # ------------------------------------------------------

    for round_number in range(1, rounds + 1):

        print("\n")
        print("=" * 60)
        print("                    ROUND", round_number)
        print("=" * 60)

        # Get user choice
        user_choice = get_user_choice()

        # Get computer choice
        computer_choice = get_computer_choice()

        # Find winner
        winner = find_winner(user_choice, computer_choice)

        # Update score
        if winner == "User":

            user_score = user_score + 1

        elif winner == "Computer":

            computer_score = computer_score + 1

        else:

            draw_score = draw_score + 1

        # Display round result
        display_round_result(
            user_choice,
            computer_choice,
            winner
        )

        # Display current score
        display_score(
            user_score,
            computer_score,
            draw_score
        )

    # Display final winner
    display_final_winner(
        user_score,
        computer_score
    )


# ----------------------------------------------------------
# FUNCTION 9: Main Program
# ----------------------------------------------------------

def main():

    while True:

        show_rules()

        play_game()

        print("\n")

        play_again = input(
            "Do you want to play again? (yes/no): "
        ).lower()

        if play_again != "yes":

            print("\n")
            print("=" * 60)
            print("Thank you for playing Rock Paper Scissors!")
            print("Have a great day!")
            print("=" * 60)

            break


# ----------------------------------------------------------
# START PROGRAM
# ----------------------------------------------------------

if __name__ == "__main__":

    main()