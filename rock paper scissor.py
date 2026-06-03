import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
print("===== ROCK PAPER SCISSORS GAME =====")
print("Rules:")
print("Rock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
while True:
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue
    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1
    print("\nScores:")
    print(f"User Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break
    else:
        continue