import random
#get user input

def play():
    user_choice = (input("Do you want 'r' Rock, 'p' Paper or 's' Scissors? ")).lower()
    if (user_choice == 'r') or (user_choice == 'rock'):
        return(f"User choice is: {user_choice}")
    elif (user_choice == 'p') or (user_choice == 'paper'):
        return(f"User choice is: {user_choice}")
    elif (user_choice == 's') or (user_choice == 'scissors'):
        return(f"User choice is: {user_choice}")
    else:
        return("Error! Not a valid choice")
#def user_choice(choice):
def get_computer_choice(computer_choice):
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        computer_choice = "rock"
        print(computer_choice)
    elif computer_choice == 1:
        computer_choice = "scissors"
        print(computer_choice)
    else:
        computer_choice = "paper"
        print(computer_choice)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"It's a tie. You both picked {computer_choice}")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("user choice wins")
    else:
        print("computer wins")

determine_winner("rock", "paper")



#use random to calculate the computer choice
#use conditionals to determine the winner

