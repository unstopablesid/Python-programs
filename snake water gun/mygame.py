
from pickle import TRUE
import random

def get_computers_choice(choice):
    choices = ["snake","water","gun"]
    get_computers_choice=random.choices(choice)
    return get_computers_choice

def my_choice(mychoice,computes_choice):
    if my_choice==get_computers_choice:
        return "it is tie"
    
    if (my_choice == 'snake' and get_computers_choice == 'water') or \
        (my_choice == 'water' and get_computers_choice == 'gun') or \
        (my_choice == 'gun' and get_computers_choice == 'snake'):
        return "You win!"
    else:
        return "You lose!"
    
def main():
    while TRUE:
        my_choice = input("enter your choice:").lower()
        if my_choice not in ["snake","water","gun"]:
            print("invalid choice")
        
    get_computers_choice = get_computers_choice()
    print(f"Computer chose: {get_computers_choice}")
    result = my_choice(my_choice, get_computers_choice)
    print(result)

if __name__ == main:
    main()