import random
import sys

# ANSI escape codes for colors
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_styled(message, color):
    print(color + message + Color.END)

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    choice = input('Choose rock, paper or scissors: ').lower()
    while choice not in choices:
        print_styled('Invalid choice. Please type exactly one of the following words: rock, paper, or scissors.', Color.RED)
        choice = input('Try again: Choose rock, paper or scissors: ').lower()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return 'It\'s a tie!'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

def ask_play_again():
    response = input('Play again? (yes/no): ').lower()
    while response not in ['yes', 'no']:
        print_styled('Invalid input. Please type "yes" or "no".', Color.RED)
        response = input('Play again? (yes/no): ').lower()
    return response == 'yes'

def main():
    print_styled('Welcome to Rock, Paper, Scissors!', Color.BLUE + Color.BOLD)
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print_styled(f'You chose: {user_choice}', Color.CYAN)
    print_styled(f'Computer chose: {computer_choice}', Color.YELLOW)
    result = determine_winner(user_choice, computer_choice)
    print_styled(result, Color.GREEN if 'win' in result else Color.RED)

    if ask_play_again():
        main()
    else:
        print_styled('Thanks for playing!', Color.PURPLE)
        sys.exit()

if __name__ == '__main__':
    main()
