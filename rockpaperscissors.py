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
        return f"Your choice is: {user_choice.capitalize()}"
    elif (user_choice == 'p') or (user_choice == 'paper'):
        user_choice = "paper"
        return f"Your choice is: {user_choice.capitalize()}"
    elif (user_choice == 's') or (user_choice == 'scissors'):
        user_choice = "scissors"
        return f"Your choice is: {user_choice.capitalize()}"
    else:
        print(f"Error! {user_choice.capitalize()} is not a valid choice. Try again.")
        return get_user_choice()


def get_computer_choice():
    global computer_choice
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        computer_choice = "rock"
        return f"Computer choice is: {computer_choice.capitalize()}"
    elif computer_choice == 1:
        computer_choice = "scissors"
        return f"Computer choice is: {computer_choice.capitalize()}"
    else:
        computer_choice = "paper"
        return f"Computer choice is: {computer_choice.capitalize()}"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"It's a tie. You both picked {computer_choice}"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return f"Yay! You won! {user_choice.capitalize()} wins against {computer_choice}"
    else:
        return f"Computer wins! {computer_choice.capitalize()} wins against {user_choice}"

def another_round():
    global play_again
    play_again = (input("Another round? Yes or no? ")).lower()
    if play_again == "yes":
        return "Yay! Let's play again!"
    elif play_again == "no":
        return "Sad to see you go, let's play again another time!"
    else:
        print("Invalid response. Please type yes or no.")
        return another_round()

print(get_rules_of_rock_paper_scissors())
print(get_user_choice())
print(get_computer_choice())
print(determine_winner(user_choice, computer_choice))
print(another_round())

while play_again == "yes":
    print(get_user_choice())
    print(get_computer_choice())
    print(determine_winner(user_choice, computer_choice))
    print(another_round())

