import random

def get_computer_choice():
    choices = ['snake', 'water', 'gun']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"

    if (player_choice == 'snake' and computer_choice == 'water') or \
       (player_choice == 'water' and computer_choice == 'gun') or \
       (player_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Snake, Water, Gun!")
    
    while True:
        player_choice = input("Enter your choice (snake, water, gun) or 'quit' to exit: ").lower()
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        if player_choice not in ['snake', 'water', 'gun']:
            print("Invalid choice. Please choose 'snake', 'water', or 'gun'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
