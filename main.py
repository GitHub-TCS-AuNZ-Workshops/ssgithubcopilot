#Write a rock, paper, scisor game
#impot random module
import random
# define main function that handles all the game logic
def main():
    # define a list of choices
    choices = ['rock', 'paper', 'scissors']
    # get the computer's choice
    computer_choice = random.choice(choices)
    # get the user's choice
    user_choice = input('Enter rock, paper, or scissors: ')
    # determine the winner
    if computer_choice == user_choice:
        print('Tie!')
    elif computer_choice == 'rock' and user_choice == 'paper':
        print('Paper covers rock! You win!')
    elif computer_choice == 'paper' and user_choice == 'scissors':
        print('Scissors cut paper! You win!')
    elif computer_choice == 'scissors' and user_choice == 'rock':
        print('Rock smashes scissors! You win!')
    elif computer_choice == 'rock' and user_choice == 'scissors':
        print('Rock smashes scissors! You lose!')
    elif computer_choice == 'paper' and user_choice == 'rock':
        print('Paper covers rock! You lose!')
    elif computer_choice == 'scissors' and user_choice == 'paper':
        print('Scissors cut paper! You lose!')
    else:
        print('I do not understand that command.')
# call the main function
main()
# define a function that gets the computer's choice


