import random
#get user input

def get_user_choice():
    global user_choice
    user_choice = (input("Do you want 'r' Rock, 'p' Paper or 's' Scissors? ")).lower()
    if (user_choice == 'r') or (user_choice == 'rock'):
        return f"User choice is: {user_choice}"
    elif (user_choice == 'p') or (user_choice == 'paper'):
        return f"User choice is: {user_choice}"
    elif (user_choice == 's') or (user_choice == 'scissors'):
        return f"User choice is: {user_choice}"
    else:
        return "Error! Not a valid choice"
#def user_choice(choice):
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

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return f"It's a tie. You both picked {computer_choice}"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return f"User wins! {user_choice} wins against {computer_choice}"
    else:
        return f"Computer wins! {computer_choice} wins against {user_choice}"

print(get_user_choice())
print(get_computer_choice())
print(determine_winner(user_choice, computer_choice))


#use random to calculate the computer choice
#use conditionals to determine the winner

