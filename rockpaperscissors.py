import random

def get_rules_of_rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    instructions = (input("Do you know the rules of the game? Type 'y' for yes and 'n' for no ")).lower()
    if (instructions == 'y') or (instructions == 'yes'):
        return "Let's play!"
    elif (instructions == 'n') or (instructions == 'no'):
        return "To play the game, you have the option to pick either rock, paper or scissors\nTo win, rock beats scissors, scissors beats paper and paper beats rock\nYour opponent is the computer, may the best player win!"
    else:
        print("Input not recognised. Please type 'y' for yes and 'n' for no.")
        return get_rules_of_rock_paper_scissors()

def get_user_choice():
    global user_choice
    user_choice = (input("Do you want 'r' Rock, 'p' Paper or 's' Scissors? ")).lower()
    if (user_choice == 'r') or (user_choice == 'rock'):
        user_choice = "rock"
        return f"Your choice is: {user_choice}"
    elif (user_choice == 'p') or (user_choice == 'paper'):
        user_choice = "paper"
        return f"Your choice is: {user_choice}"
    elif (user_choice == 's') or (user_choice == 'scissors'):
        user_choice = "scissors"
        return f"Your choice is: {user_choice}"
    else:
        print("Error! Not a valid choice.")
        return get_user_choice()

def get_computer_choice():
    global computer_choice
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        computer_choice = "rock"
        return "Computer choice is: rock"
    elif computer_choice == 1:
        computer_choice = "scissors"
        return "Computer choice is: scissors"
    else:
        computer_choice = "paper"
        return "Computer choice is: paper"

def determine_winner():
    if user_choice == computer_choice:
        return f"It's a tie. You both picked {computer_choice}"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return f"Yay! You won! {user_choice.capitalize()} wins against {computer_choice}"
    else:
        return f"Computer wins! {computer_choice.capitalize()} wins against {user_choice}"


print(get_rules_of_rock_paper_scissors())
print(get_user_choice())
print(get_computer_choice())
print(determine_winner())

