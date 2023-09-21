from text_colors import *
from colored_sentence_program import *

def ordinal_numbering(i):
    """
    Adds the correct ordinal to each number.
    """
    SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
    if 10 <= i % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(i % 10, 'th')
    ordinal_number = str(i) + suffix
    return f'\x1b[4;38;5;216m{ordinal_number}\x1b[0m'

def error_message(message):
    """
    Displays a formatted error message to the user.
    """
    print(red('Error:'), message)
    input(light_purple('Press the Enter Key to Continue. '))

def main():
    # Prompt user for the number of values to average
    while True:
        number_quantity = input('How many numbers do you have to average?: \x1b[38;5;216m')
        try:
            number_quantity = int(number_quantity)
            if number_quantity > 0:
                break
            else:
                error_message(f'You cannot average {yellow("0")} numbers. Try again.')
        except ValueError:
            error_message(f'{possible_answer(number_quantity)} is not a number. Try again.')

    # Collect the numbers to average
    numbers = []
    for i in range(number_quantity):
        number_correct = False
        while not number_correct:
            number = input(f'\x1b[0mEnter your {ordinal_numbering(i+1)} number: \x1b[38;5;216m')
            try:
                number = float(number)
                numbers.append(number)
                number_correct = True
            except ValueError:
                error_message(f'{possible_answer(number)} is not a number. Try again.')

    # Calculate the average and display it
    average = sum(numbers) / len(numbers)
    if number_quantity == 1:
        print(f'\x1b[0mThe average of this number is: \x1b[38;5;216m{average:.2f}\x1b[0m')
    else:
        print(f'\x1b[0mThe average of these numbers is: \x1b[38;5;216m{average:.2f}\x1b[0m')

if __name__ == '__main__':
    main()

