import random

def play_game():
    # Score tracking
    user_score = 0
    computer_score = 0
    while True:
        print("\nRock-Paper-Scissors Game")
        print("Enter your choice: Rock, Paper, or Scissors (or type 'quit' to exit)")
        user_choice = input("Your choice: ").strip().lower()
        if user_choice == 'quit':
            print("\nThanks for playing!")
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please select Rock, Paper, or Scissors.")
            continue
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print(f"Computer chose: {computer_choice.capitalize()}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        print(f"Current Scores - You: {user_score}, Computer: {computer_score}")
         # Ask if user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            break
play_game()