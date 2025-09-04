 # Rock-Paper-Scissors Minigame
# Specification:
# - Rock beats scissors, scissors beat paper, paper beats rock.
# - The computer is the opponent and chooses randomly between rock, paper, or scissors.
# - The player enters their choice through the console.
# - Handle invalid inputs (convert to lowercase, warn if invalid).
# - After each round, show if the player won, lost, or tied.
# - Ask if the player wants to play again.
# - Track and display the player’s score (number of wins and total rounds) at the end.

import random

# Define the valid moves
moves = ["rock", "paper", "scissors"]

# Initialize score tracking
player_wins = 0
rounds_played = 0

while True:
    # Ask player for input
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    # Validate input
    if player_choice not in moves:
        print("❌ Invalid choice! Please select rock, paper, or scissors.")
        continue

    # Computer makes a choice
    computer_choice = random.choice(moves)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if player_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "scissors" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 You win this round!")
        player_wins += 1
    else:
        print("💻 Computer wins this round!")

    # Increment rounds
    rounds_played += 1

    # Ask if player wants to continue
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

# Display final score
print("\n=== Game Over ===")
print(f"Rounds played: {rounds_played}")
print(f"Your wins: {player_wins}")
print(f"Computer wins: {rounds_played - player_wins}")
