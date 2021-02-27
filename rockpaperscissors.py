import random
#get user input

def get_user_choice(user_choice):
    user_choice = (input("Do you want 'r' Rock, 'p' Paper or 's' Scissors? ")).lower()
    if (user_choice == 'r') or (user_choice == 'rock'):
        print(f"User choice is: {user_choice}")
    elif (user_choice == 'p') or (user_choice == 'paper'):
        print(f"User choice is: {user_choice}")
    elif (user_choice == 's') or (user_choice == 'scissors'):
        print(f"User choice is: {user_choice}")
    else:
        print("Error! Not a valid choice")
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

# get_user_choice()

#use random to calculate the computer choice
#use conditionals to determine the winner

