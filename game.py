import random

def get_computer_choice():
    """Computer ko random choice deta hai"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Winner decide karta hai"""
    if user_choice == computer_choice:
        return "tie"
    
    # Winning conditions
    if user_choice == 'rock' and computer_choice == 'scissors':
        return "win"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "win"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "win"
    else:
        return "lose"

def play_game():
    """Main game function"""
    user_score = 0
    computer_score = 0
    
    print("=" * 40)
    print("Welcome to Rock Paper Scissors! 🎮")
    print("=" * 40)
    
    while True:
        print("\nYour score:", user_score)
        print("Computer score:", computer_score)
        print("\nChoices: rock, paper, scissors, quit")
        
        user_choice = input("Your choice: ").lower().strip()
        
        # Quit option
        if user_choice == 'quit':
            print("\n" + "=" * 40)
            print("Final Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            if user_score > computer_score:
                print("🎉 You WON!")
            elif computer_score > user_score:
                print("😢 Computer WON!")
            else:
                print("🤝 It's a TIE!")
            print("=" * 40)
            break
        
        # Validate input
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("❌ Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if result == "win":
            print("✅ You WON this round!")
            user_score += 1
        elif result == "lose":
            print("❌ You LOST this round!")
            computer_score += 1
        else:
            print("🤝 It's a TIE!")

if __name__ == "__main__":
    play_game()
