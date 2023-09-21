'''
*Note: Please read all the text I have provided in the terminal. Everything
is explained much better and hopefully much clearer there.

CSP (Colored Sentence Program) is a program that allows you to create,
save, and delete colored sentences. It has an introduction for new users,
but it's very long. If you want to skip it, type "s" and then "cc" or "ac"
in the main menu to view your color or action choices. 

You can create sentences, save them in existing or new files and view them in
a formatted list by typing "pr" in the main menu. You can also delete sentences
or entire files by typing "d" to access the Deletion Menu. To choose a color, you
can use built-in or custom RGB colors, which can be saved for later use. The RGB
menu is accessed by typing "rgb" in the main menu.

Beginner's Legend:
-----
first.txt: your first sentence file to save sentences
in. To change this, read the introduction.

file_accessed_number.txt: Tells the program if it
needs to first create a file before trying to use an
existing one. More info in the long intro to the program.
-
(a '0' on the first line tells the program to ask to save
a new file before asking to use an existing file. When you
create or use a file, the number on the first line in this
file automattically turns to '1'. This tells the program
that it can look for existing files in the directory.

I made it this way so that you can have manual control over if
you wanted to create a new file before you start the program.
You do not need to do this, but I tried to make the program as
customizable as possible.)

save_file: All of the txt filenames used by the program.
-
(i. e. first.txt will have its own line in this file
as "first" to tell the program it is in the CSP directory)

saved_color_codes: The saved_custom RGB ansi codes with the
name first and the ANSI code second. The program uses this
line to one, name the color and two, use the correct color
code.
-
"(i. e. "sea blue-[38;2;46;122;234m")"
-----

Sadly, because the RGB menu I have implemented into this program
is not general enough, I have not included it in text_colors.py.
You can manually make any color you wish for python files you
make with the info I found on the internet. 

Warning: If you encounter an issue where two file names in save_file.txt
combine into one line while the program is running, please stop the program
and restart it. The program will tell you what to do next. 
'''

import os, re
try:
    from text_colors import *
except ModuleNotFoundError:
    print('\x1b[91mError:\x1b[00m Please make sure to open the entire CSP folder in VS Code to run this program.')
    print('If it still doesn\'t work when you do this, Please download the CSP folder again and retry.')
    quit()

def begin_error_check():
    """
    Makes all the error checks before code starts so that I do not
    need to use so many try and except blocks in the code.

    Parameters:
    None.

    Return: None.
    """

    # Open and read the lines in file_accessed_number.txt to see
    # if the file and the required number on line one exists. If
    # anything doesn't match the needed info for this file, an
    # error is dislayed to the user.
    try:
        # Opens file_accessed_number.txt to read all the lines in
        # the file and makes sure the file only has one line
        # == 1 or 0.
        with open('file_accessed_number.txt', 'rt') as f:
            # Makes the lines of the file into a list.
            lines = f.readlines()
            if len(lines) == 0:
                # Raises an error to tell the user that
                # the file_accessed_number.txt file is
                # blank
                raise ValueError
            elif len(lines) > 1:
                # Displays this error if lines in file_accessed_number.txt is > 1
                print(red('Error:'), f'You have more than {yellow("1")} line in your {colored_file("file_accessed_number")} file. Delete the extra lines and try again.')
                print(f'Putting a {yellow("1")} on the first line in {colored_file("file_accessed_number")} means that you\'re using {colored_file("first")} or any other sentence file to save sentences in at the beginning of running the program.')
                print(f'Putting a {yellow("0")} means that you\'ve deleted {colored_file("first")} from the CSP directory and are wanting to make your own beginning sentence file.')
                quit()

            # Makes sure the one line in
            # file_accessed_number.txt is
            # a 1 or 0
            for line in f:
                if line not in ['0', '1']:
                    # Print an error saying the number in the file_accessed_number.txt file is incorrect.
                    print(red('Error:'), f'The number in your {colored_file("file_accessed_number")} is not {yellow("0")} or {yellow("1")}. Fix this and try again.')
                    print(f'Putting a {yellow("1")} on the first line in {colored_file("file_accessed_number")} means that you\'re using {colored_file("first")} or any other sentence file to save sentences in.')
                    print(f'Putting a {yellow("0")} means that you\'ve deleted {colored_file("first")} from the directory and are wanting to make your own beginning sentence file.')
                    quit()    
    except FileNotFoundError:
        # Print an error telling the user the file doesn't exist
        print(red('Error:'), f'{colored_file("file_accessed_number")} does not exist. Please download the CSP folder again and retry.')
        quit()
    except ValueError:
        # Print an error telling the user that the file_accessed_number.txt file is blank.
        print(red('Error:'), f'Your {colored_file("file_accessed_number")} is blank. Please add a number to the first line in this text file and retry.')
        print(f'Putting a {yellow("1")} on the first line in {colored_file("file_accessed_number")} means that you\'re using {colored_file("first")} or any other sentence file to save sentences in.')
        print(f'Putting a {yellow("0")} means that you\'ve deleted {colored_file("first")} from the directory and are wanting to make your own beginning sentence file.')
        quit()
    except PermissionError:
        print(red('Error:'), f'You do not have permission to read {colored_file("file_accessed_number")}.')
        print('You may try downloading the CSP folder to a location with sufficient access privileges if the issue persists.')
        quit()

    # Get a list of all the .txt files in the CSP directory
    try:
        list_of_files = []
        files = os.listdir(".")
        for txt in files:
            if txt.endswith('.txt') and txt not in ['file_accessed_number.txt', 'save_file.txt', 'saved_color_codes.txt', 'custom_rainbows.txt']:
                txt = os.path.splitext(txt)[0]
                list_of_files.append(txt.strip())
    except OSError:
        print(red('Error:'), 'unable to access the CSP directory. To fix this, please download the CSP folder again and retry.')
        quit()


    # The reason why this try block is skipped sometimes is because
    # the block is looking at the length of the lines list and the
    # list_of_files lists. There is a bug that sometimes combines
    # file names together in save_file.txt and it messes with the
    # length check. There is a try block for this bug after the
    # saved_color_code.txt file check, but I cannot seem to fix
    # this bug.

    # (The bug happens somewhere in the program, but it will
    # not crash the program when it occours. Instead, it just
    # makes the user lose access to the two conjoined file names
    # until this is fixed.)
    
    # Read words from the save_file.txt file to then make sure all
    # files are used in the program through save_file.txt
    try:
        with open('save_file.txt', 'rt') as f:
            lines = f.readlines()
        
        # Check if each text file in the directory is in the save_file.txt file
        if len(list_of_files) > len(lines):

            # Determine which files are not listed in save_file.txt
            unused_files = set(list_of_files) - set(lines)
            
            # Print the error message
            print(red('Error:'), f'{colored_file("save_file")} is missing name(s) of sentence file(s)')
            print('you have in your CSP directory. To fix this, add each missing')
            print(f'sentence filename(s) (without the file extension) on a')
            print(f'new line in {colored_file("save_file")}.')
            print()

            # Print the way to fix
            print(f'(For example, if the file {colored_file("first")} needed to be added to')
            print(f'{colored_file("save_file")}, you would write the word "first" on a new')
            print(f'line in {colored_file("save_file")} and save the file.)')
            input(light_purple('Press the Enter key to Continue. '))
            print()

            # Print what's missing in save_file.txt
            print(f'The following file(s) in the CSP directory are not listed in {colored_file("save_file")}:')
            max_item_length = len(max(unused_files, key=len)) + 7
            print('-' * max_item_length)
            for i, filename in enumerate(unused_files):
                print(f'{list_num_color(f"{i + 1}." )} {colored_file(filename.strip())}')
            print('-' * max_item_length)
            tip('Continuing will not crash the program.')
            warning_message('Until this is changed, continuing will result in the inability to access the above files in the program.')
            
            # Ask the user if they want to continue anyway.
            okay_to_continue_correct = 'n'
            while okay_to_continue_correct == 'n':
                print()
                okay_to_continue = input('Continue anyway? (y/n): ')
                if okay_to_continue in ['no', 'n']:
                    print('Quitting Now..')
                    quit()
                elif okay_to_continue in ['yes', 'y']:
                    okay_to_continue_correct = 'y'
                    input(light_purple('Press the Enter key to Continue. '))
                    print()
                else:
                    print()
                    yn_typo_error(okay_to_continue)

        # Check if each word in the file is a text file in the CSP directory.
        elif len(list_of_files) < len(lines):

            # Determine which lines in save_file.txt are not used
            unused_lines = lines[len(list_of_files):]

            # Print the error message
            print(red('Error:'), f'{colored_file("save_file")} has excess sentence filename(s) than what')
            print(f'will be used in the program. To fix this, remove the extra')
            print(f'filename(s) from {colored_file("save_file")}.')
            print()

            # Print the solution to this problem
            print(f'(For example, if the word "first" was in {colored_file("save_file")},')
            print(f'and you don\'t have a file named {colored_file("first")} in the CSP directory,')
            print('you would delete that line and save the file.)')
            input(light_purple('Press the Enter key to Continue.'))
            
            # Show the user what extra lines exist in save_file.txt
            print()
            print(f"The following line(s) in {colored_file('save_file')} do not correspond with a text file in the CSP directory:")
            max_item_length = len(max(unused_lines, key=len)) + 5
            print('-' * max_item_length)
            for i, line in enumerate(unused_lines):
                print(f'{list_num_color(f"{i + 1}." )} "{line.strip()}"')
            print('-' * max_item_length)
            tip('You will be able to run the program when this problem is fixed.')
            quit()


    except PermissionError:
        print(red('Error:'), f'You do not have permission to read {colored_file("save_file")}.')
        print('You may try downloading the CSP folder to a location with sufficient access privileges if the issue persists.')
        quit()
    except FileNotFoundError:
        print(red('Error:'), f'{colored_file("save_file")} does not exist. Please download the CSP folder again and retry.')
        quit()
    
    
    # See if saved_color_codes.txt file exists
    try:
        if not os.path.exists('saved_color_codes.txt'):
            raise FileNotFoundError
    except FileNotFoundError:
        print(red('Error:'), f'{colored_file("saved_color_codes")} does not exist. Please download the CSP folder again and retry.')
        quit()
    
    # Check to see if all .txt files are used in the program
    try:
        with open('save_file.txt', 'rt') as f:
            filenames = f.readlines()
            for filename in filenames:
                filename = filename.strip()
                
                # Checks if the filename is in the CSP directory
                if not os.path.exists(f'{filename}.txt'):
                    print(red('Error:'), f'{colored_file(filename)} does not exist. Please make sure every file name in {colored_file("save_file")} is')
                    print(f'on its own line and without the file extension. Then try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    print()
                    warning_message(f'Occasionally, the program doesn\'t press the enter key when writing new files to {colored_file("save_file")}.')
                    print('(I am unsure as to why this is the case, so if this happens, just press enter between the combined')
                    print('file names, and you\'ll be good to go.)')
                    quit()
    except FileNotFoundError:
        print(red('Error:'), f'{colored_file("save_file")} does not exist. Please download the CSP folder again and retry.')
        quit()
    except PermissionError:
        print(red('Error:'), f'You do not have permission to use {colored_file(filename)}.')
        print('You may try downloading the CSP folder to a location with sufficient access privileges if the issue persists.')
        quit()
    if not os.path.exists('custom_rainbows.txt'):
        print(red('Error:'), f'{colored_file("custom_rainbows")} does not exist. Please download the CSP folder again and retry.')
        quit()
    
def instructions():
    """
    runs through the instructions of this program.

    Parameters:
    None

    Return: None.
    """
    print()
    print('----')
    print('VS Code has a color system that allows the user to color the text being sent..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('to this print box. (Or terminal)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('I have made a program that uses this system without the use of a third party module.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('(Such as colorama)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('So now you can use this feature in VS Code without one.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('If you just want to use the functions, go ahead!')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('This feature only works with software that supports it.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('Such as VS Code')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('(Notice that if you try to open this program with the python program directly, the color will not show up.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('(Instead, the colors are replaced with the invisible characters that create the color in VS code.)')
    input(light_purple('Press the Enter key to Continue. '))
    print('----')
    print()
    print('If you know a little about Python you\'ll see that I used..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('non-variable inputs to split up this text.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('So, even if you type anything in them, nothing will happen.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('---')
    print('As you go through this program, tips will show up in light purple; Such as the one below:')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('While running this program, you may also come across something like this:')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    warning_message('This is an example')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('To get passed these, just follow their instructions.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('Try it now: ')
    warning_message('This is an example. To move on, press the enter key on the message below:')
    input('I am a message: ').lower()
    print()
    print('Good.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('Error messages look like warnings, but they are red. Like this:')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(red('--TYPO ERROR:'), f'{possible_answer("example")} is an invalid answer. Try again.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('Moving on..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('In this program, you will be able to make your sentences any color.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('Then, you can save those sentences in sentence files.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('You can then view, change or delete these sentence files..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('with some actions I have provided.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('You can access every action or color through the main menu.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'You can also type {possible_answer("none")} in any field to cancel specific requests.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'(Look above the field to check if it is possible in that specific field.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('This is because I couldn\'t spend the time to set it up any other way.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('The text you enter in will return colorized..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('And then you can save it to a file of your choice.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('There are eleven possible color choices in this program that will return colored text.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('The colors you can access through the main menu are:')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('-' * 40)
    print('1. ' + red('RED -'), 'changes the color of your sentence to red.')
    print(f'(You can access this color by typing: {possible_answer("r")} or {possible_answer("red")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('2. ' + yellow('YELLOW -'), 'changes the color of your sentence to yellow.')
    print(f'(You can access this color by typing: {possible_answer("y")} or {possible_answer("yellow")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('3. ' + green('GREEN -'), 'changes the color of your sentence to green.')
    print(f'(You can access this color by typing: {possible_answer("g")} or {possible_answer("green")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('4. ' + light_purple('LIGHT PURPLE -'), 'changes the color of your sentence to light purple.')
    print(f'(You can access this color by typing: {possible_answer("lp")} or {possible_answer("light purple")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('5. ' + purple('PURPLE -'), 'changes the color of your sentence to purple.')
    print(f'(You can access this color by typing: {possible_answer("p")} or {possible_answer("purple")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('6. ' + cyan('CYAN/BLUE -'), 'changes the color of your sentence to cyan/blue.')
    print(f'(You can access this color by typing: {possible_answer("c")}, {possible_answer("cyan/bue")}, {possible_answer("cyan")}, or {possible_answer("b")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('7. ' + light_gray('LIGHT GRAY -'), 'changes the color of your sentence to light gray.')
    print(f'(You can access this color by typing: {possible_answer("lg")}, {possible_answer("light gray")}, or {possible_answer("white")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('8. ' + gray('GRAY -'), 'changes the color of your sentence to gray.')
    print(f'(You can access this color by typing: {possible_answer("g")} or {possible_answer("gray")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('9. ' + rainbow_words('RAINBOW WORDS -'), f'changes each word in your sentence into the next color of the rainbow, starting with the color {red("red")}.')
    print(f'(You can access this color by typing: {possible_answer("rw")} or {possible_answer("rainbow words")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('10. ' + rainbow_letters('RAINBOW LETTERS -'), f'changes each letter in your sentence into it\'s own rainbow, starting with the color {red("red")}.')
    print(f'(You can access this color by typing: {possible_answer("rl")} or {possible_answer("rainbow letters")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('11. ' + title_custom_color('CUSTOM COLOR -'), f'changes the color of your sentence based on an {red("R")}{green("G")}{cyan("B")} value given.')
    print(f'(You can access this color by typing: {possible_answer("custom color")}, {possible_answer("custom")} or {possible_answer("rgb")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'-    (to find out how {red("R")}{green("G")}{cyan("B")} values work, you can go online for more info.)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (There is a whole {red("R")}{green("G")}{cyan("B")} menu in this program. You can {possible_answer("delete")}, use {possible_answer("existing")}, or make {possible_answer("new")} colors to write sentences with.)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (When creating a new color, you will give the {red("R")}{green("G")}{cyan("B")} values and then you\'ll be asked what you want that color text to say.')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (However, unlike other times, it asks you if you want to save a color you use if it is new.)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (Whether you say {possible_answer("y")} or {possible_answer("n")}, you\'ll be able to save that sentence after that block. That was the only way I could fit it in.)')
    print('-' * 40)
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('The actions you can access through the main menu are:')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('-' * 40)
    print('1. ' + cyan('PRINT -'), 'Prints any sentence file with it\'s sentences in a list I formatted.')
    print(f'(You can access this action by typing: {possible_answer("pr")} or {possible_answer("print")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'-    (to choose a file to print, you will need to type out the file name without the {purple(".txt")} file extension)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print('2. ' + cyan('DELETE -'), 'Deletes either unwanted sentences in a sentence file or deletes an entire sentence file.')
    print(f'(You can access this action by typing: {possible_answer("d")}, {possible_answer("df")}, {possible_answer("delete file")}, {possible_answer("delete sentence")}, {possible_answer("sentence")}, or {possible_answer("delete")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'-    (When deleting a sentence from a sentence file, you choose the corresponding sentence number.)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (When deleting an entire file, you will need to type out the file name without the {purple(".txt")} file extension)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print('3. ' + cyan('COLOR CHOICES -'), 'If at any time you want to see your color choices again.')
    print(f'(You can access this action by typing: {possible_answer("cc")}, or {possible_answer("color choices")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('4. ' + cyan('ACTION CHOICES -'), 'If at any time you want to see your action choices again.')
    print(f'(You can access this action by typing: {possible_answer("ac")}, or {possible_answer("action choices")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('5. ' + cyan('SAVING SENTENCES -'), 'Save any sentence you make to a file.')
    print(f'(Happens automatically when you are done creating your sentence.)')
    print('-' * 40)
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('You can make different files to save your sentences in.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'You will start out this program by automatically using the {colored_file("first")} file as a base file to save sentences.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'If you don\'t want to start by using the {colored_file("first")} file..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'You can replace the {yellow(f"1")} in {colored_file("file_accessed_number")}..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'with a {yellow(f"0")}, delete all the words in {colored_file("save_file")}..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'delete all unwanted files from the folder that all your saved sentences are in..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'(If you have any)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'and finally, save EVERYTHING before you start the program again.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'If you did these steps right, it will tell the program that you have no text files to save to.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'The program will then help you create a new file.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'Also, as an accidental perk, this program allows you to save your sentence in your last used file.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'(unless you don\'t have one to save to)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'How cool is that?')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'If you find any bugs, tell me.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'There is a random bug that occasionally forgets to press the enter key..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'between a new file name and the last one in {colored_file("save_file")}.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'Just press enter between the two merged text file names and you\'re good to go.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    warning_message('(make sure you\'re deleting the right file or sentence before you say yes to anything)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    warning_message('I am not responsible for any accidentally deleted sentences or sentence files.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    warning_message('If you make any manual changes to a file..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    warning_message('Be sure to save it before running the program again.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    warning_message('If the program doesn\'t work after manually changing a file..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    warning_message(f'You will need to download the CSP folder again.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('All dashes on the top and bottom of a list is sized..')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('according to the biggest item in that list.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('Anyway, that\'s it. Enjoy!')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(red('© Kaden Hansen. All Rights Reserved.'))
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('(Not really)')
    input(light_purple('Press the Enter key to Continue. '))

def instruction_introduction():
    """
    Introduces the program, then asks
    if the user wants the instructions.

    Parameters:
    None

    Return: None.    
    """
    # title screen
    print(rainbow_words('Welcome to the Colored Sentence Program!'))
    print()
    print(yellow('------------------------------------------------------------'.center(0)))
    print(yellow(f"Be sure to make your terminal fullscreen by pressing the {cyan('^')}".center(70)))
    print(yellow(f"button in the terminal as well as hit the {cyan('f11')} {yellow('key to get the')}".center(67)))
    print(yellow(f'best experience.'.center(60)))
    print(yellow('------------------------------------------------------------'.center(0)))
    
    # asking the user if they want the instructions
    want_instructions_correct = 'n'
    while want_instructions_correct == 'n':
        print()

        # Give the necessary tips and warnings for the upcoming question
        print('---')
        warning_message('This introduction is very long.')
        tip('It\'s only necessary if you want a detailed overview of all the available features.')
        tip('Available actions and colors are accessible through the main menu.')
        tip(f'You can type {possible_answer(f"skip")} or {possible_answer(f"s")} in the field below to skip this part.')
        print('---')
        print()

        # Ask the user if they want to see the instructions.
        want_instructions = input('Do you wish to see the introduction? (y/n/s): ').lower()
        if want_instructions == 'y':
            instructions()
            want_instructions_correct = 'y'
        elif want_instructions == 'none':
            main()
            make_the_sentence_again()
        elif want_instructions in ['skip', 's']:
            want_instructions_correct = 'y'
            main()
        elif want_instructions == 'n':
            want_instructions_correct = 'y'

            # Warning the user that they may need to look at the instructions if it's their first time going through this program
            continue_correct = 'n'
            while continue_correct == 'n':
                print()
                warning_message('If you do not know what your color choices are, you may need to look at the instructions to find out.')
                continue_ = input('Are you sure you want to continue without looking at the instructions? (y/n): ').lower()
                if continue_ == 'n':
                    print('Here they are:')
                    print()
                    continue_correct = 'y'
                    instructions()
                    want_instructions_correct = 'y'
                elif continue_ == 'y':
                    print('Moving on..')
                    continue_correct = 'y'
                    want_instructions_correct = 'y'
                else:
                    print()
                    yn_typo_error(continue_)
                    input(light_purple('Press the Enter key to Continue. '))

        else:
            print()
            print(red('--TYPO ERROR:'), f'{possible_answer(want_instructions)} did not match the expected {possible_answer("y")}, {possible_answer("n")}, or {possible_answer("s")} answers. Try again.')
            input(light_purple('Press the Enter key to Continue. '))
# All the "make life easy" functions
def yn_typo_error(question_answer):
    """
    prints a formatted typo error string for a yes or no question.
    
    Parameters:
    question_answer = the answer the user gave
    
    Return: None.
    """
    print(red('--TYPO ERROR:'), f'{possible_answer(question_answer)} did not match the expected {possible_answer("y")} or {possible_answer("n")} answers. Try again.')

def possible_answer(answer):
    """
    Possible answers shown to the user
    will show up as cyan.

    Parameters:
    answer: The item being colorized and
    shown to the user.

    Return: None.
    """
    thing = (cyan(f'"{answer}"'))
    return thing

def warning_message(warning_message):
    """
    prints a warning message to the user.

    Parameters:
    warning_message = the warning message you wish to display to the user.
    
    Return: None.
    """
    print(yellow('--WARNING:'), f'{warning_message}')

def check_if_file_has_been_accessed():
    """
    checks the file_accessed_number.txt document to see
    what the number is on line 1.
    
    Parameters:
    None

    returns the value of the number of line one in the text document
    """
    # getting number from file_accessed_number.txt for pathway
    with open('file_accessed_number.txt', 'rt') as f:
    # If the f file has a 0 on the first line
        for line in f:
            if line == '':
                f.write('0')
            if line == '0':
                file_accessed = 0
            else:
                file_accessed = 1   
    return file_accessed

def tip(tip_message):
    """
    Create a tip for the user by entering the text you wish to display.
    
    Parameters:
    tip_message: the tip you wish to give the user

    Return: None.
    """

    print(f'{light_purple("--TIP:")} {tip_message}')

def list_num_color(number):
    """
    Applies a custom color to the
    list numbers.

    Parameters:
    number: The number to color.

    returns the number with a custom color.
    """
    
    number_color = "\x1b[38;2;160;239;0m{}\x1b[00m".format(number)
    return number_color

def title_custom_color(text):
    """
    Gets a custom color and
    applies it to specified
    text.

    Parmeters:
    text: text to convert.

    returns a colored string
    """
    custom_text = '\x1b[38;2;255;34;114m{}\x1b[0m'.format(text)
    return custom_text

def colored_file(file_name):
    """
    Turns any file_name to purple to help the user better understand what is happening to the files.

    Parameters:
    file_name: The file name that will turn purple.

    returns a colored string like:
    """
    colored_file = f'{purple(f"{file_name}.txt")}'

    return colored_file
# End of "make life easy" functions
def save_sentence_sequence(final_sentence):
    """
    runs through the sequence to save the sentence.
    
    This is NOT the one to write new files directly.
    create_new_file_q is the one to make the file.
    This one just asks the user what they want to do
    with their new sentence.
    
    Parameters:
    final_sentence: the sentence that needs to run through this function

    Return: None.
    """
    
    # save_sentence error handling
    save_sentence_correct = 'n'
    while save_sentence_correct == 'n':
            print()
            save_sentence_question = input('Would you like to save your sentence in a new file? (y/n): ').lower()
            # if the user wants to save the file
            if save_sentence_question == 'y':
                save_sentence_correct = 'y'
                # file name maker  
                file_name_correct = 'n'
                while file_name_correct == 'n':
                    print()
                    tip(f'the {purple(".txt")} file extension will be applied automatically.')
                    file_name = input('What would you like to call this file?: ').lower()
                    # file_name user error handling
                    invalid_character_counter = 0
                    valid_character_count = 0
                    file_name_correct = 'y'
                    invalid_character_list = [ '/', '\\', '<', '>', '|', '?', ':', '*', '.']
                    # checking if any character in the string is an invalid one
                    # If there are, the name doesn't pass
                    for letter in file_name:
                        for character in invalid_character_list:
                            if letter == character:
                                invalid_character = character
                                print()
                                print(red('--TYPO ERROR:'), f'your file name cannot contain a {possible_answer(invalid_character)}. Try again.')
                                input(light_purple('Press the Enter key to Continue. '))
                                invalid_character_counter += 1
                            elif letter != character:
                                valid_character_count += 1
                            if invalid_character_counter > 0:
                                file_name_correct = 'n'  
                            # end of file_name_error_handling
                    # do only if string has no invalid characters
                    if invalid_character_counter != 1:
                        # final_file_correct error handling
                        # final_file_correct error handling
                        with open('save_file.txt', 'rt') as sf_read:
                            lines = sf_read.readlines()
                        for line in lines:
                            cleanline = line.strip()
                            if cleanline == file_name:
                                file_name_correct = 'n'
                                print()
                                print(red('Error:'), f'{colored_file(file_name)} already exists. Try again.')
                                input(light_purple('Press the Enter key to Continue. '))
                                break
                            else:
                                file_name_correct = 'y'
                        if file_name_correct != 'n':
                            file_compare = f'{file_name}.txt'
                            files = os.listdir(".")
                            for filename in files:
                                if file_compare == filename:
                                    file_name_correct = 'n'
                                    print()
                                    print(red('Error:'), f'{colored_file(file_name)} already exists. Try again.')
                                    input(light_purple('Press the Enter key to Continue. '))
                                    break
                            else:
                                file_name_correct = 'y'
                        if file_name_correct == 'y':
                            final_file_correct1 = 0
                            while final_file_correct1 == 0:
                                print()
                                tip(f'You can type {possible_answer(f"none")} in the field below to cancel this request.')
                                final_file = input(f'Are you sure you want to call your file {colored_file(file_name)}? (y/n): ').lower()
                                if final_file == 'y':
                                    save_sentence(file_name=file_name, sentence=final_sentence)
                                    save_file(file_name=file_name)
                                    print()
                                    print(green('--SUCCESS:'), f'Your sentence has been saved in', colored_file(file_name) + '.')
                                    print(f'You will be able to find your file in the folder with both program files.')
                                    input(light_purple('Press the Enter key to Continue. '))
                                    print()
                                    tip('You can access your saved sentences even when the program stops running. Go to the instructions for more info.')
                                    input(light_purple('Press the Enter key to Continue. '))
                                    file_accessed_()
                                    final_file_correct1 = 1
                                    save_sentence_correct = 'y'
                                    file_name_correct = 'y'
                                    make_the_sentence_again()
                                elif final_file == 'n':
                                    file_name_correct = 'n'
                                    final_file_correct1 = 1
                                else:
                                    print()
                                    yn_typo_error(final_file)
                                    input(light_purple('Press the Enter key to Continue. '))
                        else:
                            print()
                            warning_message(f'Because an error has occurred, you\'ll need to confirm')
                            print('that you want to create a new file again. If you don\'t want')
                            print(f'to create a new file, please type {possible_answer("n")}.')
                            
                            input(light_purple('Press the Enter key to Continue. '))
                            save_sentence_sequence(final_sentence)           
            elif save_sentence_question == 'n':
                print()
                wish_to_continue_correct = 'n'
                while wish_to_continue_correct == 'n':
                    warning_message('You are about to discard this sentence because you do not have any documents to save this sentence to.')
                    wish_to_continue = input('Are you sure you don\'t want to save this sentence? (y/n): ').lower()
                    if wish_to_continue == 'y':
                        wish_to_continue_correct = 'y'
                        print()
                        warning_message('Your sentence has not been saved')
                        make_the_sentence_again()
                    elif wish_to_continue == 'n':
                        file_name = 'first'
                        print()
                        print('--')
                        tip(f'You said you were wanting to save this sentence, so, it has been saved in a default text file called {colored_file(file_name)}.')
                        tip(f'If you don\'t like this name, you will need to change it manually in the file explorer and in {colored_file("save_file")}.')
                        print('--')
                        print()
                        save_sentence(file_name=file_name, sentence=final_sentence)
                        print(green('--AUTO SAVE:'), f'Because you weren\'t sure about deleting your sentence,')
                        print(f'it has been backed up to {colored_file(file_name)}. You can find it in this program\'s main folder.')
                        input(light_purple('Press the Enter key to Continue. '))
                        print()
                        tip('You can access your saved sentences even when the program stops running. Go to the instructions for more info.')
                        input(light_purple('Press the Enter key to Continue. '))
                        print()
                        final_file_correct1 = 1
                        invalid_character_counter = 0
                        wish_to_continue_correct = 'y'
                        save_sentence_correct = 'n'
                        make_the_sentence_again()
                    else:
                        print()
                        yn_typo_error(wish_to_continue)
                        input(light_purple('Press the Enter key to Continue. '))
            else:
                print()
                yn_typo_error(save_sentence_question)
                input(light_purple('Press the Enter key to Continue. '))

def ssc(setting, final_sentence):
    """
    Asks the user how they want to save their sentence
    if at all.

    This is the main one. save_sentence_sequence() is to save
    a new sentence to a newly created file because no file names
    are existant in save_file.txt

    Parameters:
    setting: the setting the user chose to type their sentence in.

    Such as: 
    red, yellow, green, light purple, purple, cyan/blue, light gray,
    gray, rainbow words, and rainbow letters, or custom colors

    final_sentence: the sentence the user typed in one of the above
    colors.
    
    Return: None.
    """
    # If the setting is print, we don't want to activate this function as there is no sentence to save.
    if setting not in ['print', 'pr']:
        # getting number from file_accessed_number.txt to see if the user has files created or not.
        file_accessed = check_if_file_has_been_accessed()
        # Error handling for yes_save_sentence
        yes_save_sentence = 'n'
        while yes_save_sentence == 'n':
        # asking the user if they want to save their sentence. 
            tip('This question is asking if you want to save your sentence in general.')
            yes_save_sentence = input('Would you like to save your sentence? (y/n): ')
            # If the user wants to save their sentence.
            if yes_save_sentence == 'y':
                # If the f file has a 0 on the first line
                if file_accessed == 0:
                    save_sentence_sequence(final_sentence=final_sentence)
                # If the f file has a 1 on the first line
                elif file_accessed == 1:
                    # Open save_file and get the name on the last line
                    with open('save_file.txt', 'rt') as f:
                        for line in f:
                            file_name = line.strip()
                    save_sentence_correct = 'n'
                    while save_sentence_correct == 'n':
                        print()
                        # Ask the user if they want to use their last file they used to save their sentence.
                        save_sentence_question = input(f'Would you like to save your sentence in your {colored_file(file_name)} file? (y/n): ').lower()
                        if save_sentence_question == 'y':
                            save_sentence_correct = 'y'
                            print()
                            # save the sentence to the last used .txt file.
                            save_sentence(file_name=file_name, sentence=final_sentence)
                            # Tell the user of the success
                            print(green('--SUCCESS:'), f'Your sentence has been saved in', colored_file(file_name) + '.')
                            print(f'You will be able to find your file in the folder with both program files.')
                            input(light_purple('Press the Enter key to Continue. '))
                            print()
                            tip('You can access your saved sentences even when the program stops running. Go to the instructions for more info.')
                            input(light_purple('Press the Enter key to Continue. '))
                            make_the_sentence_again()
                        elif save_sentence_question == 'n':
                            like_to_open_another_file_correct = 'n'
                            while like_to_open_another_file_correct == 'n':
                                print()
                                # Ask the user if they want to add their sentence to an existing file in the CSP directory.
                                like_to_open_another_file = input('Would you like to add your sentence to an existing file? (y/n): ').lower()
                                if like_to_open_another_file == 'y':
                                    # Open save_file.txt and read what's in there to show the available files you can save the sentence to.
                                    with open('save_file.txt', 'rt') as fi:
                                        list_of_texts = []
                                        for i, line in enumerate(fi):
                                            list_of_texts.append(line.strip())
                                        # Gets the longest item in the list to match the dash size to that.
                                        max_item_length = len(max(list_of_texts, key=len)) + 7
                                    choice_of_text_correct = 'n'
                                    while choice_of_text_correct == 'n':
                                        if len(list_of_texts) == 0:
                                            # Prints a formatted list
                                            print('Available text documents you can add your sentence to:'.center(40))
                                            print('-' * 35)
                                            print('You have no existing text documents')
                                            print('-' * 35)
                                            choice_of_text_correct = 'y'
                                            tip('You will need to create some text files before you can add your sentence to it')
                                            input(light_purple('Press the Enter Key to try to save your sentence again.'))
                                            # runs this portion of the code again because the user cannot save their file to a nonexisting file.
                                            print()
                                            sentence_length = len(f'Your colorized sentence is: {final_sentence}') - 10
                                            print('-' * sentence_length)
                                            print(f'Your colorized sentence is:', final_sentence)
                                            print('-' * sentence_length)
                                            ssc(setting=setting, final_sentence=final_sentence)
                                        else:
                                            print()
                                            # prints a formatted list with helpful information
                                            print('Available text documents you can add your sentence to:'.center(40))
                                            print('-' * max_item_length)
                                            for i, line in enumerate(list_of_texts):
                                                if line != '\n':
                                                    print(f'{list_num_color(i + 1)}. {purple((f"{line}.txt"))}')
                                            print('-' * max_item_length)
                                            tip(f'You can type {possible_answer("none")} to cancel this request.')
                                            print()
                                            tip(f'The {purple(".txt")} file extension will be applied automatically.')
                                            choice_of_text = input(f'Which text document do you wish to add your sentence to?: ').lower()
                                            if choice_of_text == 'none':
                                                print()
                                                warning_message('Taking you back..')
                                                input(light_purple('Press the Enter key to Continue. '))
                                                sentence_length = len(f'Your colored sentence is: {final_sentence}') - 10
                                                print()
                                                print('-' * sentence_length)
                                                print(f'Your colored sentence is:', final_sentence)
                                                print('-' * sentence_length)
                                                ssc(setting='g', final_sentence=final_sentence)
                                            if choice_of_text in list_of_texts:
                                                file_name = choice_of_text
                                                choice_of_text_correct = 'y'
                                                sure_to_append_to_file = 'n'
                                                while sure_to_append_to_file == 'n':
                                                    print()
                                                    sure_to_append_to_file = input(f'Are you sure you want to add your sentence to {colored_file(file_name)}? (y/n): ').lower()
                                                    if sure_to_append_to_file == 'y':
                                                        print()
                                                        save_sentence(file_name=file_name, sentence=final_sentence)
                                                        print(green('--SUCCESS:'), f'Your sentence has been saved in', colored_file(file_name) + '.')
                                                        print(f'You will be able to find your file in the folder with both program files.')
                                                        input(light_purple('Press the Enter key to Continue. '))
                                                        print()
                                                        tip('You can access your saved sentences even when the program stops running. Go to the instructions for more info.')
                                                        input(light_purple('Press the Enter key to Continue. '))
                                                        make_the_sentence_again()
                                                        save_sentence_correct = 'y'
                                                    elif sure_to_append_to_file == 'n':
                                                        sure_to_append_to_file = 'y'
                                                        choice_of_text_correct = 'n'
                                                    else:
                                                        print()
                                                        yn_typo_error(sure_to_append_to_file)
                                                        input(light_purple('Press the Enter key to Continue. '))
                                                        sure_to_append_to_file = 'n'
                                            elif choice_of_text not in list_of_texts:
                                                print()
                                                print(red('--TYPO ERROR:'), f'{possible_answer(choice_of_text)} does not match any documents shown above. Try again.')
                                                input(light_purple('Press the Enter key to Continue. '))
                                                print()
                                            elif choice_of_text == 'none':
                                                make_the_sentence_again()
                                                sure_to_append_to_file = 'n'
                                    print()
                                elif like_to_open_another_file == 'n':
                                        print()
                                        make_new_file_correct = 'n'
                                        while make_new_file_correct == 'n':
                                            create_new_file_q(final_sentence=final_sentence)
                                else:
                                    print()
                                    yn_typo_error(like_to_open_another_file)                    
                                    input(light_purple('Press the Enter key to Continue. '))
                        else:
                            print()
                            yn_typo_error(save_sentence_question)
                            input(light_purple('Press the Enter key to Continue. '))
                            print()
            elif yes_save_sentence == 'n':
                yes_save_sentence = 'y'
                wish_to_continue_correct = 'n'
                while wish_to_continue_correct == 'n':
                    print()
                    warning_message('You are about to discard this sentence.')
                    wish_to_continue = input('Are you sure you don\'t want to save this sentence? (y/n): ').lower()
                    if wish_to_continue == 'y':
                        wish_to_continue_correct = 'y'
                        print()
                        warning_message('Your sentence has not been saved.')
                        input(light_purple('Press the Enter key to Continue. '))
                        make_the_sentence_again()
                    elif wish_to_continue == 'n':
                        file_name = 'first'
                        wish_to_continue_correct = 'y'
                        save_sentence(file_name=file_name, sentence=final_sentence)
                        print(green('--AUTO SAVE:'), f'Because you weren\'t sure about deleting your sentence,')
                        print(f'it has been backed up to {colored_file(file_name)}. You can find it in this program\'s main folder.')
                        input(light_purple('Press the Enter key to Continue. '))
                        print()
                        tip('You can access your saved sentences even when the program stops running. Go to the instructions for more info.')
                        input(light_purple('Press the Enter key to Continue. '))
                        print()
                        make_the_sentence_again()
                    else:
                        print()
                        yn_typo_error(wish_to_continue)
                        input(light_purple('Press the Enter key to Continue. '))
                        yes_save_sentence = 'n'
            else:
                print()
                yn_typo_error(yes_save_sentence)
                input(light_purple('Press the Enter key to Continue. '))
                print()
                yes_save_sentence = 'n'
                sentence_length = len(f'Your new colorized sentence is: {final_sentence}') - 10
                print('-' * sentence_length)
                print(f'Your new colorized sentence is:', final_sentence)
                print('-' * sentence_length)        

def color_choices():
    """
    Displays the available color choices to the user.

    Parameters:
    None

    Return: None.    
    """
    print()
    print('There are eleven possible color choices in this program that will return colored text.')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('The colors you can access through the main menu are:')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('-' * 40)
    print('1. ' + red('RED -'), 'changes the color of your sentence to red.')
    print(f'(You can access this color by typing: {possible_answer("r")} or {possible_answer("red")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('2. ' + yellow('YELLOW -'), 'changes the color of your sentence to yellow.')
    print(f'(You can access this color by typing: {possible_answer("y")} or {possible_answer("yellow")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('3. ' + green('GREEN -'), 'changes the color of your sentence to green.')
    print(f'(You can access this color by typing: {possible_answer("g")} or {possible_answer("green")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('4. ' + light_purple('LIGHT PURPLE -'), 'changes the color of your sentence to light purple.')
    print(f'(You can access this color by typing: {possible_answer("lp")} or {possible_answer("light purple")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('5. ' + purple('PURPLE -'), 'changes the color of your sentence to purple.')
    print(f'(You can access this color by typing: {possible_answer("p")} or {possible_answer("purple")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('6. ' + cyan('CYAN/BLUE -'), 'changes the color of your sentence to cyan/blue.')
    print(f'(You can access this color by typing: {possible_answer("c")}, {possible_answer("cyan/bue")}, {possible_answer("cyan")}, or {possible_answer("b")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('7. ' + light_gray('LIGHT GRAY -'), 'changes the color of your sentence to light gray.')
    print(f'(You can access this color by typing: {possible_answer("lg")}, {possible_answer("light gray")}, or {possible_answer("white")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('8. ' + gray('GRAY -'), 'changes the color of your sentence to gray.')
    print(f'(You can access this color by typing: {possible_answer("g")} or {possible_answer("gray")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('9. ' + rainbow_words('RAINBOW WORDS -'), f'changes each word in your sentence into the next color of the rainbow, starting with the color {red("red")}.')
    print(f'(You can access this color by typing: {possible_answer("rw")} or {possible_answer("rainbow words")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('10. ' + rainbow_letters('RAINBOW LETTERS -'), f'changes each letter in your sentence into it\'s own rainbow, starting with the color {red("red")}.')
    print(f'(You can access this color by typing: {possible_answer("rl")} or {possible_answer("rainbow letters")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('11. ' + title_custom_color('CUSTOM COLOR -'), f'changes the color of your sentence based on an {red("R")}{green("G")}{cyan("B")} value given.')
    print(f'(You can access this color by typing: {possible_answer("custom color")}, {possible_answer("custom")} or {possible_answer("rgb")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'-    (to find out how {red("R")}{green("G")}{cyan("B")} values work, you can go online for more info.)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (There is a whole {red("R")}{green("G")}{cyan("B")} menu in this program. You can {possible_answer("delete")}, use {possible_answer("existing")}, or make {possible_answer("new")} colors to write sentences with.)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (When creating a new color, you will give the {red("R")}{green("G")}{cyan("B")} values and then you\'ll be asked what you want that color text to say.')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (However, unlike other times, it asks you if you want to save this color.)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (Whether you say {possible_answer("y")} or {possible_answer("n")}, you\'ll be able to save that sentence after that block. That was the only way I could fit it in.)')
    print('-' * 40)
    input(light_purple('Press the Enter key to Continue. '))

def rgb_menu_sequence():
    """
    The sequence of functions used to correctly
    maneuver through the RGB menu.

    Parameters:
    None.

    Return: None.
    
    """
    rgb = custom_color_maker()
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    color_code = use_color(r=r, g=g, b=b)
    sentence_color_example(color_code)
    custom_color_applier(color_code=color_code)
    make_the_sentence_again()

def action_choices():
    """
    Prints the actions the user can use.

    Parameters:
    None

    Return: None.
    """
    print()
    print('The actions you can access through the main menu are:')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('-' * 40)
    print('1. ' + cyan('PRINT -'), 'Prints any sentence file with it\'s sentences in a list.')
    print(f'(You can access this action by typing: {possible_answer("pr")} or {possible_answer("print")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'-    (to choose a file to print, you will need to type out the file name without the {purple(".txt")} file extension)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print('2. ' + cyan('DELETE -'), 'Deletes either unwanted sentences in a sentence file or deletes an entire sentence file.')
    print(f'(You can access this action by typing: {possible_answer("d")}, {possible_answer("df")}, {possible_answer("delete file")} or {possible_answer("delete")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print(f'-    (When deleting a sentence from a sentence file, you choose the corresponding sentence number.)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print(f'-    (When deleting an entire file, you will need to type out the file name without the {purple(".txt")} file extension)')
    input(light_purple('      Press the Enter key to Continue. '))
    print()
    print('3. ' + cyan('COLOR CHOICES -'), 'If at any time you want to see your color choices again.')
    print(f'(You can access this action by typing: {possible_answer("cc")}, or {possible_answer("color choices")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('4. ' + cyan('ACTION CHOICES -'), 'If at any time you want to see your action choices again.')
    print(f'(You can access this action by typing: {possible_answer("ac")}, or {possible_answer("action choices")} in the main menu.)')
    input(light_purple('Press the Enter key to Continue. '))
    print()
    print('5. ' + cyan('SAVING SENTENCES -'), 'Save any sentence you make to a file.')
    print(f'(Happens automatically when you are done creating your sentence.)')
    print('-' * 40)
    input(light_purple('Press the Enter key to Continue. '))
    print()

def custom_color_maker():
    """
    Asks the user for an RGB value and then
    makes a color code that then is accessed
    by custom_color_applier() to add this
    color to the text.

    Parameters:
    text: text to convert

    Return: None.
    """
    pick_where_to_get_color_correct = 'n'
    while pick_where_to_get_color_correct == 'n':
        print()
        print(red('R') + green('G') + cyan('B'), title_custom_color('Menu:'))
        print('---')
        tip(f'You can type {possible_answer("delete")} or {possible_answer("d")} in the field below to delete a saved color.')
        tip(f'You can type {possible_answer("none")} to cancel this request.')
        print('---')
        print()
        pick_where_to_get_color = input(f'Do you want to use an {possible_answer("existing")} color or a {possible_answer("new")} color?: ').lower()
        if pick_where_to_get_color in ['existing', 'e']:
            pick_where_to_get_color_correct == 'y'
            print_saved_colors()
            rgb_menu_sequence()
        elif pick_where_to_get_color in ['d', 'delete']:
            pick_where_to_get_color_correct == 'y'
            delete_saved_color()
            make_the_sentence_again()
        elif pick_where_to_get_color in ['new', 'n']:
            pick_where_to_get_color_correct == 'y'
            color_code_correct = 'n'
            while color_code_correct == 'n':
                print()
                print('Enter the following color information:')
                try:
                    print()
                    warning_message('A numerical error will only occur after all the color values are entered.')
                    r = int(input(f'Enter the {red("red")} value (0-255): '))
                    print()
                    g = int(input(f'Enter the {green("green")} value (0-255): '))
                    print()
                    b = int(input(f'Enter the {cyan("blue")} value (0-255): '))
                    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                        color_code_correct = 'y'
                    else:
                        print()
                        warning_message('Invalid RGB value. Please enter a value between 0 and 255.')
                        color_code_correct = 'n'
                        input(light_purple('Press the Enter key to Continue. '))
                except ValueError:
                    print()
                    warning_message('Invalid input. Please enter a valid integer.')
                    input(light_purple('Press the Enter key to Continue. '))
                    color_code_correct = 'n'
            return [r, g, b]
        elif pick_where_to_get_color == 'none':
            print()
            warning_message('No action will be taken.')
            input(light_purple('Press the Enter key to Continue. '))
            make_the_sentence_again()
        else:
            print()
            print(red('--TYPO ERROR:'), f'{possible_answer(f"{pick_where_to_get_color}")} does not match any of the above values. Try again.')
            input(light_purple('Press the Enter key to Continue. '))

def use_color(r, g, b):
    """
    Makes sure the user wants
    to use the color they chose.

    Parameters:
    r (int): a value between 0-255 
    g (int): a value between 0-255 
    b (int): a value between 0-255 
    
    Return: None.
    """
    # make variable for while loop
    sure_want_to_use_color = 'n'
    while sure_want_to_use_color == 'n':
        # Asks the user if their RGB input is what they meant to do.
        print()
        want_to_use_color = input(f'Are these the correct {red("R")}{green("G")}{cyan("B")} values?: {red(r)}, {green(g)}, {cyan(b)} (y/n): ')
        # If the RGB input is correct
        if want_to_use_color == 'y':
            color_code = '\x1b[38;2;{};{};{}m'.format(r, g, b)
            sure_want_to_use_color = 'y'
        
        # If the RGB input isn't correct
        elif want_to_use_color == 'n':
            rgb = custom_color_maker()
            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            color_code = '\x1b[38;2;{};{};{}m'.format(r, g, b)
        # If the user doesn't type "y" or "n"
        else:
            print()
            print(red('--TYPO ERROR:'), f'{possible_answer(want_to_use_color)} did not match the expected {possible_answer("y")} or {possible_answer("n")} answers. Try again.')
            input(light_purple('Press the Enter key to Continue. '))
    return color_code

def create_custom_rainbow_list():
    """
    Allows the user to create a custom list of rainbow colors using RGB codes.
    Returns a list of ANSI color codes that can be used with the rainbow functions.

    Parameters:
    None.

    Return: A list of colors.
    """
    num_colors_correct = 'n'
    while num_colors_correct == 'n':
        print()
        num_colors = input('How many colors do you want to add to this rainbow?: ')
        if num_colors.lower() == 'none':
            print()
            warning_message('No custom rainbow will be made.')
            input(light_purple('Press the Enter key to Continue. '))
            make_the_sentence_again()
        try:
           num_colors = int(num_colors)
        except ValueError:
            print()
            print(red('Error:'), f'{possible_answer(num_colors)} is not a valid number. Try again.')
            input(light_purple('Press the Enter key to Continue. '))
            continue
        
        if num_colors > 14:
            print()
            print(red('Error:'), f'Your rainbow cannot have more than {yellow("14")} colors in it.')
            input(light_purple('Press the Enter key to Continue. '))
            continue
        elif num_colors <= 0:
            print()
            print(red('Error:'), f'Your rainbow cannot have {yellow("0")} colors in it.')
            input(light_purple('Press the Enter key to Continue. '))
            continue
        elif num_colors <= 2:
            print()
            print(red('Error:'), f'You need at least {yellow("3")} colors to make a rainbow silly!')
            input(light_purple('Press the Enter key to Continue. '))
            continue
          
        sure_num_colors_correct = 'n'
        while sure_num_colors_correct == 'n':
            print()
            sure_num_colors = input(f'Are you sure you want this custom letters\' rainbow to have {yellow(num_colors)} colors in it? (y/n): ').lower()
            if sure_num_colors == 'y':
                colors = []
                i = 0
                while i < num_colors:
                    color_code_correct = 'n'
                    while color_code_correct == 'n':
                        print()
                        print(f'Enter the following {red("R")}{green("G")}{cyan("B")} information for \033[4;39mcolor {i + 1}\x1b[0m:')
                        try:
                            rgb_correct = 'n'
                            while rgb_correct == 'n':
                                print()
                                warning_message('A numerical error will only occur after all the color values are entered.')
                                r = int(input(f'Enter the {red("red")} value (0-255): '))
                                print()
                                g = int(input(f'Enter the {green("green")} value (0-255): '))
                                print()
                                b = int(input(f'Enter the {cyan("blue")} value (0-255): '))
                                if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                                    rgb_correct = 'y'
                                    color_code_correct = 'y'
                                    sure_color_code_correct = 'n'
                                    while sure_color_code_correct == 'n':
                                        print()
                                        sure_color_code = input(f'Are these {red("R")}{green("G")}{cyan("B")} correct?: {red(r)}, {green(g)}, {cyan(b)} (y/n): ').lower()
                                        if sure_color_code == 'y':
                                            sure_color_code_correct = 'y'
                                            rgb_correct = 'y'
                                            color_code_correct = 'y'
                                            num_colors_correct = 'y'
                                            sure_num_colors_correct = 'y'
                                            color_code = '\x1b[38;2;{};{};{}m'.format(r, g, b)
                                            colors.append(color_code)
                                            i += 1
                                        else:
                                            rgb_correct == 'n'
                                            sure_color_code_correct = 'y'
                                            color_code_correct = 'n'
                                else:
                                    print()
                                    warning_message('Invalid RGB value. Please enter a value between 0 and 255.')
                                    color_code_correct = 'n'
                                    input(light_purple('Press the Enter key to Continue. '))
                        except ValueError:
                            print()
                            warning_message('Invalid input. Please enter a valid integer.')
                            input(light_purple('Press the Enter key to Continue. '))
                            color_code_correct = 'n'
            elif sure_num_colors == 'n':
                create_custom_rainbow_list()
            elif sure_num_colors.lower() == 'none':
                print()
                warning_message('Taking you back..')
                input(light_purple('Press the Enter key to Continue. '))
                create_custom_rainbow_list()
        return colors

def give_rainbow_name():
    """
    Asks the user if they want to name this rainbow
    before it is saved.

    Parameters:
    None.

    Return: custom rainbow name.
    """
    give_rainbow_name_correct = 'n'
    while give_rainbow_name_correct == 'n':
        print()
        give_rainbow_name = input('Do you want to give this rainbow a name? (y/n): ').lower()
        if give_rainbow_name == 'y':
            rainbow_name_correct = 'n'
            while rainbow_name_correct == 'n':
                print()
                rainbow_name = input('What do you want to call this rainbow?: ').lower()
                sure_rainbow_name_correct = 'n'
                while sure_rainbow_name_correct == 'n':
                    print()
                    sure_rainbow_name = input(f'Are you sure you want to call this rainbow "{rainbow_name.title()}"? (y/n): ').lower()
                    if sure_rainbow_name == 'y':
                        return rainbow_name
                    elif sure_rainbow_name == 'n':
                        sure_rainbow_name_correct = 'y'
                        rainbow_name_correct = 'n'
                    else:
                        print()
                        yn_typo_error()
        elif give_rainbow_name == 'n':
            return None
        else:
            print()
            yn_typo_error(give_rainbow_name)

def save_rainbow(rainbow_name, colors, save):
    """
    Saves the new custom rainbow to custom_rainbows.txt

    Parameters:
    rainbow_name: The name of the rainbow.
    colors: The list of colors to save
    save: a yes or no response to see if
    the user really wants to save their newly
    made rainbow.
    """
    if save == 'yes':
        if rainbow_name == None:
            with open('custom_rainbows.txt', 'rt') as cr_read:
                lines = cr_read.readlines()
                for i, _ in enumerate(lines):
                    rainbow_name = f'rainbow_{i + 2}'
        with open('custom_rainbows.txt', 'at') as cr_append:
            cr_append.write(f'{rainbow_name}-{colors}\n')
        print()
        print(green('--SUCCESS:'), f'Your new rainbow has been saved to {colored_file(f"custom_rainbows")}')
        print(f'You will be able to access this rainbow by typing {possible_answer("e")} in the Custom Rainbow Maker.')
        input(light_purple('Press the Enter key to Continue. '))
        custom_rainbow_menu()

def pick_rainbow_to_delete():
    """
    Allows the user to pick a saved
    rainbow and delete it.

    Parameters:
    None.

    Return: The line in the custom_rainbows.txt file the user wants to delete.
    """
    import ast

    rainbow_lists_list = []
    rainbow_names_list = []
    list_numbers = []

    with open('custom_rainbows.txt', 'rt') as cr_read:
        lines = cr_read.readlines()

    for line in lines:
        name, colors_str = line.split('-')
        colors_str = colors_str.strip()
        colors_list = ast.literal_eval(colors_str)
        rainbow_lists_list.append(colors_list)
        rainbow_names_list.append(name.strip())
    if len(lines) == 0:
        print()
        max_item_length = len('You do not have any saved custom rainbows in custom_rainbows.txt')
        print('Available rainbows you can delete:'.center(max_item_length))
        print('-' * max_item_length)
        print(f'You do not have any saved custom rainbows in {colored_file("custom_rainbows")}')
        print('-' * max_item_length)
        tip('You will need to add some rainbows to access them.')
        input(light_purple('Press the Enter key to Continue. '))
        custom_rainbow_menu()
    else:
        max_item_length = len(max(rainbow_names_list, key=len)) + 6 + len(max(rainbow_names_list, key=len))
        print()
        print('Available rainbows you can delete are:')
        print('-' * max_item_length)
        for i, (name, colors_list) in enumerate(zip(rainbow_names_list, rainbow_lists_list)):
            print(f'{list_num_color(f"{i + 1}.")}', f'{custom_rainbow_letters(name.title(), colors_list)} - {custom_rainbow_words(name.title(), colors_list)}')
            list_numbers.append(str(f'{i + 1}'))
        print('-' * max_item_length)
        tip(f'You can type {possible_answer("none")} in the field below to cancel this request.')
        delete_rainbow_correct = 'n'
        while delete_rainbow_correct == 'n':
            print()
            tip('You can type either the list number listed above or the rainbow name.')
            delete_rainbow = input('Which custom rainbow do you want to delete?: ')
            if delete_rainbow == 'none':
                print()
                warning_message('No rainbow will be deleted.')
                input(light_purple('Press the Enter key to Continue. '))
                custom_rainbow_menu()
            if delete_rainbow in rainbow_names_list or delete_rainbow in list_numbers:
                sure_want_delete_rainbow_correct = 'n'
                while sure_want_delete_rainbow_correct == 'n':
                    print()
                    if delete_rainbow in list_numbers:
                        sure_want_delete_rainbow = input(f'Are you sure you want to delete rainbow {yellow(delete_rainbow)}? (y/n): ').lower()
                    elif delete_rainbow in rainbow_names_list:
                        sure_want_delete_rainbow = input(f'Are you sure you want to delete your "{(delete_rainbow)}" rainbow? (y/n): ').lower()
                    if sure_want_delete_rainbow == 'none':
                        print()
                        warning_message('No rainbow will be used.')
                        input(light_purple('Press the Enter key to Continue. '))
                        custom_rainbow_menu()
                    if sure_want_delete_rainbow == 'y':
                        return delete_rainbow
                    elif sure_want_delete_rainbow == 'n':
                        sure_want_delete_rainbow_correct = 'y'
                        delete_rainbow_correct = 'n'
                    else:
                        print()
                        yn_typo_error(sure_want_delete_rainbow)
                        input(light_purple('Press the Enter key to Continue. '))
            else:
                print()
                print(red('Error:'), f'{possible_answer(delete_rainbow)} does not match any saved rainbow. Try again.')
                input(light_purple('Press the Enter key to Continue. '))
                pick_rainbow_to_delete()

def delete_rainbow(delete_rainbow):
    """
    Deletes the selected rainbow from
    custom_rainbow.txt

    Parameters:
    delete_rainbow: The rainbow name to delete
    
    Return: the response to see if it was deleted or not.
    """
    import ast
    delete_color = []
    not_delete_colors = []

    with open('custom_rainbows.txt', 'rt') as cr_read:
        lines = cr_read.readlines()
        lines_len = len(lines)
    
    for i, line in enumerate(lines):
        name, colors = line.split('-')
        if delete_rainbow == name or delete_rainbow == str(i + 1):
            colors = colors.strip()
            colors = ast.literal_eval(colors)
            delete_color.append(f'{name}-{colors}\n')
        else:
            colors = colors.strip()
            colors = ast.literal_eval(colors)
            not_delete_colors.append(f'{name}-{colors}\n')

    with open('custom_rainbows.txt', 'wt') as cr_write:
        cr_write.write('')
    with open('custom_rainbows.txt', 'at') as cr_append:
        for i, string in enumerate(not_delete_colors):
            cr_append.write(string)
    
    with open('custom_rainbows.txt', 'rt') as cr_read:
        lines = cr_read.readlines()
        if len(lines) < lines_len:
            return 'deleted'
        else:
            return 'not'
            
def display_if_deleted(response):
    """
    Tells the user if the rainbow
    they wanted to delete was in
    fact, deleted.

    Parameters:
    response: the return from delete_rainbow.

    Return:
    None.
    """
    if response == 'deleted':
        print()
        print(green('SUCCESS:'), f'Your rainbow has been successfully deleted.')
        print(f'You will no longer be able to find the rainbow in {colored_file("custom_rainbows")}.')
        input(light_purple('Press the Enter key to Continue. '))
    else:
        print()
        print(red('Error:'), f'Your rainbow was not deleted from {colored_file("custom_rainbows")} because')
        print(f'an error occured. Please contact me for help.')
        input(light_purple('Press the Enter key to Continue. '))
        
def print_existing_rainbows():
    """
    Prints the saved rainbows in a formatted
    list for the user to choose the rainbow
    they want to use.

    Parameters:
    None.

    Return: The rainbow to use.
    """
    import ast

    rainbow_lists_list = []
    rainbow_names_list = []
    list_numbers = []

    with open('custom_rainbows.txt', 'rt') as cr_read:
        lines = cr_read.readlines()

    for line in lines:
        name, colors_str = line.split('-')
        colors_str = colors_str.strip()
        colors_list = ast.literal_eval(colors_str)
        rainbow_lists_list.append(colors_list)
        rainbow_names_list.append(name.strip())
    if len(lines) == 0:
        print()
        max_item_length = len('You do not have any saved custom rainbows in custom_rainbows.txt')
        print('Available rainbows you can use are:'.center(max_item_length))
        print('-' * max_item_length)
        print(f'You do not have any saved custom rainbows in {colored_file("custom_rainbows")}')
        print('-' * max_item_length)
        tip('You will need to add some rainbows to access them.')
        input(light_purple('Press the Enter key to Continue. '))
        custom_rainbow_menu()
    else:    
        max_item_length = len(max(rainbow_names_list, key=len)) + 6 + len(max(rainbow_names_list, key=len))
        print()
        print('Available rainbows you can use are:')
        print('-' * max_item_length)
        for i, (name, colors_list) in enumerate(zip(rainbow_names_list, rainbow_lists_list)):
            print(f'{list_num_color(f"{i + 1}.")}', f'{custom_rainbow_letters(name.title(), colors_list)} - {custom_rainbow_words(name.title(), colors_list)}')
            list_numbers.append(str(f'{i + 1}'))
        print('-' * max_item_length)
        tip(f'You can type {possible_answer("none")} in the field below to cancel this request.')
        choice_rainbow_correct = 'n'
        while choice_rainbow_correct == 'n':
            print()
            tip('You can type either the list number listed above or the rainbow name.')
            choice_rainbow = input('Which custom rainbow do you want to use?: ')
            if choice_rainbow == 'none':
                print()
                warning_message('No rainbow will be used.')
                input(light_purple('Press the Enter key to Continue. '))
                custom_rainbow_menu()
            if choice_rainbow in rainbow_names_list or choice_rainbow in list_numbers:
                sure_want_use_rainbow_correct = 'n'
                while sure_want_use_rainbow_correct == 'n':
                    print()
                    if choice_rainbow in rainbow_names_list:
                        sure_want_use_rainbow = input(f'Are you sure you want to use "{choice_rainbow}"? (y/n): ').lower()
                    elif choice_rainbow in list_numbers:
                        sure_want_use_rainbow = input(f'Are you sure you want to use rainbow {yellow(choice_rainbow)}? (y/n): ').lower()
                    if sure_want_use_rainbow == 'none':
                        print()
                        warning_message('No rainbow will be used.')
                        input(light_purple('Press the Enter key to Continue. '))
                        custom_rainbow_menu()
                    elif sure_want_use_rainbow == 'y':
                        return choice_rainbow
                    elif sure_want_use_rainbow == 'n':
                        sure_want_use_rainbow_correct = 'y'
                        choice_rainbow_correct = 'n'
                    else:
                        print()
                        yn_typo_error(sure_want_use_rainbow)
                        input(light_purple('Press the Enter key to Continue. '))
            else:
                print()
                print(red('Error:'), f'{possible_answer(choice_rainbow)} does not match any saved rainbow. Try again.')
                input(light_purple('Press the Enter key to Continue. '))
                print_existing_rainbows()

def use_custom_rainbow(rainbow_answer):
    """
    Allows the user to use the rainbow
    they have chosen to make their sentence
    either go in rainbow word or rainbow
    letter form

    Parameters:
    rainbow_answer: The rainbow to use

    Return: The colored string
    """
    import ast

    with open('custom_rainbows.txt', 'rt') as cr_read:
        lines = cr_read.readlines()
    
    for i, line in enumerate(lines):
        name, colors = line.split('-')
        if rainbow_answer == name or rainbow_answer == str(i + 1):
            colors = colors.strip()
            colors = ast.literal_eval(colors)
            colors_to_use = colors
            name_to_use = name
    rainbow_type_correct = 'n'
    while rainbow_type_correct == 'n':
        print()
        tip(f'Your {rainbow_letters("rainbow options")} are either {custom_rainbow_letters("letters", colors_to_use)} or {custom_rainbow_words("words", colors_to_use)}.')
        rainbow_type = input('What type of rainbow do you wish to use with this custom rainbow?: ').lower()
        if rainbow_type in ['word', 'w']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {custom_rainbow_words(f"{name_to_use} words", colors_to_use)} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', custom_rainbow_letters(text_to_convert, colors_to_use))
                    print('-' * sentence_length)
                    final_sentence = custom_rainbow_letters(text_to_convert, colors)
                    ssc(setting='cr', final_sentence=final_sentence)
        elif rainbow_type in ['l', 'letters']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {custom_rainbow_letters(f"{name_to_use} letters", colors_to_use)} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', custom_rainbow_letters(text_to_convert, colors_to_use))
                    print('-' * sentence_length)
                    final_sentence = custom_rainbow_letters(text_to_convert, colors_to_use)
                    ssc(setting='cr', final_sentence=final_sentence)
        elif rainbow_type == 'none':
            print()
            warning_message('No rainbow will be chosen.')
            input(light_purple('Press the Enter key to Continue. '))
            custom_rainbow_menu()
        else:
            print()
            print(red('Typo Error:'), f'{possible_answer(rainbow_type)} is not a valid rainbow type. Try again.')
            input(light_purple('Press the Enter key to Continue. '))


def custom_rainbow_words(text, colors):
    """
    Colors the words one by one in the
    text provided in repeating colors
    word by word that the user chose.

    Parameters:
    text: text to convert
    colors: the colors to use in the rainbow
    
    Return: rainbow text by word
    """
    # make the 'text' string into a list
    text_list = re.findall(r'\S+|\s+', text)

    # create a list of colors for each letter in the input text
    rainbow_letter_list = []
    current_color = colors[0]
    for i in range(len(text_list)):
        if text_list[i] == ' ':
            rainbow_letter_list.append(' ')
        else:
            # Apply the current color to the current word, then get the next
            # color in the color list to apply it to the next word. Basically,
            # current_color is first, used on the current word, and then
            # updated to be the current index in the colors list + 1 % len(colors)
            # to get the next item in the colors list. It then also makes sure that
            # the new index stays within range of the length of the color list.
            colored_letter = current_color + text_list[i]
            rainbow_letter_list.append(colored_letter)
            current_color = colors[(colors.index(current_color) + 1) % len(colors)]

    # combine colored letters into the final rainbow string
    rainbow_string = ''.join(rainbow_letter_list)

    # resets text color to default
    rainbow_string += '\x1b[0m'

    # return the rainbow string
    return rainbow_string

def custom_rainbow_letters(text, colors):
    """
    Colors the words one by one in the
    text provided in repeating colors
    letter by letter that the user chose.

    Parameters:
    text: text to convert
    colors: the colors to use in the rainbow
    
    Return: rainbow text by letter
    """
    # split the input text into a list of letters
    letter_list = list(text)

    # create a list of colors for each letter in the input text
    rainbow_letter_list = []
    current_color = colors[0]
    for i in range(len(letter_list)):
        if letter_list[i] == ' ':
            # if the current character is a space, don't color it
            rainbow_letter_list.append(' ')
        else:
            # Apply the current color to the current letter, then get the next
            # color in the color list to apply it to the next letter. Basically,
            # current_color is first, used on the current letter, and then
            # updated to be the current index in the colors list + 1 % len(colors)
            # to get the next item in the colors list. It then also makes sure that
            # the new index stays within range of the length of the colors list.
            colored_letter = current_color + letter_list[i]
            rainbow_letter_list.append(colored_letter)
            current_color = colors[(colors.index(current_color) + 1) % len(colors)]

    # combine colored letters into the final rainbow string
    rainbow_string = ''.join(rainbow_letter_list)

    # reset color to default
    rainbow_string += '\x1b[0m'

    # return the rainbow string
    return rainbow_string

def show_rainbow(colors):
    """
    Show the user an example of the new
    rainbow before it is saved.

    Parameters:
    colors (list): the list of color codes
    to be used for the custom letters and
    words functions as examples printed to
    the user

    Return: 'yes' or 'no'.
    """
    print()
    max_item_length = 44
    print('Text Examples Using Your New Rainbow:'.center(max_item_length))
    print('-' * max_item_length)
    print('Rainbow Words:'.center(max_item_length))
    print('----'.center(max_item_length))
    print(custom_rainbow_words('The quick brown fox jumps over the lazy dog.', colors))
    print('----'.center(max_item_length))
    input(light_purple('Press the Enter key to Continue.'.center(max_item_length)))
    print()
    print('Rainbow Letters:'.center(max_item_length))
    print('----'.center(max_item_length))
    print(custom_rainbow_letters('The quick brown fox jumps over the lazy dog.', colors))
    print('----'.center(max_item_length))
    input(light_purple('Press the Enter key to Continue.'.center(max_item_length)))
    print()
    print('-' * max_item_length)
    tip(f'You can type {possible_answer("none")} in the field below')
    print('to cancel this request.')
    save_my_rainbow_correct = 'n'
    while save_my_rainbow_correct == 'n':
        print()
        save_my_rainbow = input('Do you want to save this rainbow? (y/n): ').lower()
        if save_my_rainbow == 'y':
            return 'yes'
        elif save_my_rainbow == 'n':
            print()
            warning_message('Your rainbow has not been saved.')
            input(light_purple('Press the Enter key to Continue. '))
            print()
            warning_message('Taking you back.')
            input(light_purple('Press the Enter key to Continue. '))
            custom_rainbow_menu()
        elif save_my_rainbow == 'none':
            print()
            warning_message('The rainbow was not saved.')
            input(light_purple('Press the Enter key to Continue. '))
            custom_rainbow_menu()
        else:
            print()
            yn_typo_error(save_my_rainbow)
            input(light_purple('Press the Enter key to Continue. '))

def custom_rainbow_menu():
    """
    The menu for the custom rainbow
    maker.

    Parameters:
    None.

    Return: None.
    """
    print()
    which_rainbow_action_correct = 'n'
    while which_rainbow_action_correct == 'n':
        print(f'{title_custom_color("Custom Rainbow Menu:")}')
        print('---')
        tip(f'Type {possible_answer("new")} or {possible_answer("existing")} depending on what you want below.')
        tip(f'To delete a custom rainbow, type {possible_answer("delete")} in the field below.')
        print('---')
        print()
        which_rainbow_action = input('Which action do you want to do?: ').lower()
        if which_rainbow_action in ['d', 'delete']:
            rainbow_d = pick_rainbow_to_delete()
            response = delete_rainbow(rainbow_d)
            display_if_deleted(response)
            make_the_sentence_again()
        elif which_rainbow_action in ['n', 'new']:
            which_rainbow_action_correct = 'y'
            colors = create_custom_rainbow_list()
            save = show_rainbow(colors)
            rainbow_name = give_rainbow_name()
            save_rainbow(rainbow_name, colors, save)
            which_rainbow_action_correct = 'n'
        elif which_rainbow_action in ['e', 'existing']:
            rainbow_choice = print_existing_rainbows()
            use_custom_rainbow(rainbow_choice)
            custom_rainbow_menu()
        elif which_rainbow_action == 'none':
            print()
            warning_message('No action will be taken.')
            input(light_purple('Press the Enter key to Continue. '))
            make_the_sentence_again()

def sentence_color_example(color_code):
    """
    Shows the user an example sentence with
    the color they chose.

    Parameters:
    color_code: The code to apply to the
    example sentence.

    Return: None.
    """
    print()
    print('Example sentence using your color: '.center(43))
    print('-' * 44)
    print('{}The quick brown fox jumps over the lazy dog.{}'.format(color_code, "\x1b[0m"))
    print('-' * 44)
    ask_to_save_color_code(color_code)

def custom_color_applier(color_code, color_name = None):
    """
    Changes the color of the text to
    the custom RGB color. 

    Parameters:
    color_code: the color to
    apply to the text.

    color_name: To ask the user
    what they want their new
    saved color is in other functions.
    (default: None)

    Returns final_sentence.
    """
    print()
    if color_name == None:
        text_to_convert = input('What do you want the {}custom{} text to say?: '.format(color_code, "\x1b[0m"))
    else:
        text_to_convert = input('What do you want the {}{}{} text to say?: '.format(color_code, color_name, "\x1b[0m"))
    if len(text_to_convert) > 150:
        print()
        warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
        input(light_purple('Press the Enter key to Continue. '))
    elif len(text_to_convert) == 0:
        print()
        warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
        input(light_purple('Press the Enter key to Continue. '))
    if text_to_convert == 'none':
        print()
        warning_message('Taking you back..')
        input(light_purple('Press the Enter key to Continue. '))
        rgb_menu_sequence()
    if len(text_to_convert) < 150 and len(text_to_convert) > 0:
        colorized_text = "{}{}\x1b[0m".format(color_code, text_to_convert)
        sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
        print()
        print('-' * sentence_length)
        print(f'Your new colorized sentence is:', colorized_text)
        print('-' * sentence_length)
        final_sentence = colorized_text
    return final_sentence

def ask_to_save_color_code(color_code):
    """
    Asks the user if they want to save a color
    to a file and if they do, asks for a name,
    then it saves it to saved_color_codes.txt.

    Parameters:
    color_code: the color to save to the file.
    """
    want_save_color_code_correct = 'n'
    while want_save_color_code_correct == 'n':
        print()
        want_save_color_code = input('Do you want to save this color for future use? (y/n): ').lower()
        if want_save_color_code == 'y':
            print()
            give_color_name_correct = 'n'
            while give_color_name_correct == 'n':
                give_color_name = input('Do you want to give this color a name? (y/n): ').lower()
                if give_color_name == 'y':
                    print()
                    color_called = input('What do you want to call this color?: ')
                    sure_want_save_color_code_correct = 'n'
                    while sure_want_save_color_code_correct == 'n':
                        print()
                        sure_color_called = input('Are you sure you want to call this color {}? (y/n): '.format(color_code + color_called + "\x1b[0m")).lower()
                        if sure_color_called == 'y':
                            save_color_code(color_name=color_called, color_code=color_code)
                            final_sentence = custom_color_applier(color_name=color_called, color_code=color_code)
                            ssc(setting='rgb', final_sentence=final_sentence)
                        elif sure_color_called == 'n':
                            print()
                            warning_message('{} will not be saved.'.format(color_code + color_called + "\x1b[0m"))
                            input(light_purple('Press the Enter key to Continue. '))
                            print()
                            custom_color_applier(color_code)
                        else:
                            print()
                            yn_typo_error(sure_color_called)
                            input(light_purple('Press the Enter key to Continue. '))
                elif give_color_name == 'n':
                    save_color_code(color_code=color_code)
                    print()
                    final_sentence = custom_color_applier(color_code=color_code)
                    ssc(setting='rgb', final_sentence=final_sentence)
                else:
                    print()
                    yn_typo_error(give_color_name)
                    input(light_purple('Press the Enter key to Continue. '))
        elif want_save_color_code == 'n':
            print()
            warning_message('Your color will not be saved.')
            input(light_purple('Press the Enter key to Continue. '))
            final_sentence = custom_color_applier(color_code=color_code)
            ssc(setting='rgb', final_sentence=final_sentence)
        else:
            print()
            yn_typo_error(want_save_color_code)
            input(light_purple('Press the Enter key to Continue. '))    

def save_color_code(color_code, color_name = None):
    """
    Saves color to saved_color_codes.txt with
    a name the user chooses. If the user doesn't
    give a name, one is generated based on the
    amount of lines in the file.

    color_code: the color code to save to the file.
    color_name (default: None): The name of the color. 
    (ex. if 3 lines exist in saved_color_codes.txt
    then the saved color_name will be "color_4")
    """
    if not os.path.exists('saved_color_codes.txt'):
        with open('saved_color_codes.txt', 'wt') as scc_w:
            scc_w.write('')
    else:
        color_codes = []
        if color_name != None:
            with open('saved_color_codes.txt', 'at') as scc_a:
                scc_a.write(f'{color_name.lower()}-')
                scc_a.write(f'{color_code}\n')
        elif color_name == None:
            with open('saved_color_codes.txt', 'rt') as scc_r:
                for line in scc_r:
                    color_codes.append(line.strip())
            color_name = f'color_{len(color_codes) + 1}'
            with open('saved_color_codes.txt', 'at') as scc_a:
                scc_a.write(f'{color_name.lower()}-')
                scc_a.write(f'{color_code}\n')
    print()
    print(green('--SUCCESS:'), '{} has been saved to {}'.format(color_code + color_name + "\x1b[0m", colored_file(f"saved_color_codes")))
    print(f'You will be able to use this color by typing {possible_answer("existing")} when')
    print('asked what you want to do in the RGB menu.')
    input(light_purple('Press the Enter key to Continue. '))

def print_saved_colors():
    """
    Prints saved colors from the
    saved_color_codes.txt
    
    Parameters:
    None

    Return: None.
    """
    if not os.path.exists('saved_color_codes.txt'):
        with open('saved_color_codes.txt', 'wt') as scc_w:
            scc_w.write('')
    color_codes = []
    color_names = []
    with open('saved_color_codes.txt', 'rt') as scc_r:
        for line in scc_r:
            color_codes.append(line.strip())
    max_length = 0
    for line in color_codes:
        name, code = line.split('-')
        len_line = len(name) + 3
        if len_line > max_length:
            max_length = len_line
    if len(color_codes) == 0:
        print()
        print('Available color codes you can use:'.center(63))
        print('-' * 63)
        print(f'You do not have any saved color codes in {colored_file("saved_color_codes")}.')
        print('-' * 63)
        tip('You will need to add colors to use them.')
        input(light_purple('Press the Enter key to Continue. '))
    else:
        print()
        print('Available color codes you can use:')
        print()
        print('-' * max_length)
        for i, line in enumerate(color_codes):
            name, code = line.split('-')
            color_names.append(name.strip())
            print(f'{list_num_color(f"{i + 1}.")}', code + name.title() + "\x1b[0m")
        print('-' * max_length)
        tip(f'You can type {possible_answer("none")} in the field below to cancel this request.')
        warning_message(f'You will need to type the full color name to access it.')
        pick_from_saved_colors(main_list=color_codes)
            
def pick_from_saved_colors(main_list):
    """
    Allows the user to pick the color
    they want to use in their sentence.

    Parameters:
    None

    Return: None.
    """
    color_codes = []
    color_names = []
    pick_color_to_use_correct = 'n'
    while pick_color_to_use_correct == 'n':
        print()
        pick_color_to_use = input('Which color do you want to use?: ').lower()
        for item in main_list:
            color_name, color_code = item.split('-')
            color_codes.append(color_code.strip().lower())
            color_names.append(color_name.strip().lower())
        for code, name in zip(color_codes, color_names):
            used_number = 0
            if used_number != 1:
                if name == pick_color_to_use:
                    color_to_use = name
                    used_number = 1
                    break
                else:
                    color_to_use = ''
        if pick_color_to_use == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    rgb_menu_sequence()
        if pick_color_to_use == color_to_use:
            final_sentence = custom_color_applier(color_code=code, color_name=color_to_use.title())
            ssc(final_sentence=final_sentence, setting="rgb")
            make_the_sentence_again()
        else:
            print()
            print(red('--TYPO ERROR:'), f'The {possible_answer(pick_color_to_use)} color does not exist. Try again.')
            input(light_purple('Press the Enter key to Continue. '))

def delete_saved_color():
    """
    Opens a delete color menu for the
    user if they wish to delete a saved
    custom color.
    
    Parameters:
    None

    Return: None.
    """
    with open('saved_color_codes.txt', 'rt') as scc_r:
        color_names = []
        color_codes = []
        item_list = []
        for item in scc_r:
            item_list.append(item.strip())
            name, code = item.split('-')
            color_names.append(name.strip())
            color_codes.append(code.strip())
    if len(color_names) == 0:
        print()
        print(f'The colors you can delete are:'.center(51))
        print('-' * 51)
        print(f'There are no colors saved in {colored_file("saved_color_codes")}.')
        print('-' * 51)
        tip(f'You will need to create colors to delete them.')
    elif len(color_names) >= 1:
        max_item_length = 0
        for line in color_names:
            len_line = len(line)
            if len_line > max_item_length:
                max_item_length = len_line + 3
        print()
        print(f'The colors you can delete are:')
        print()
        print('-' * max_item_length)
        for i, line in enumerate(color_names):
            print('{} {}'.format(list_num_color(f"{i + 1}."), color_codes[i] + line.title() + "\x1b[0m"))
        print('-' * max_item_length)
        tip(f'You can type {possible_answer("none")} in the field below to cancel this request.')
        warning_message(f'You will need to type the full color name to access it.')
        delete_selected_color_correct = 'n'
        while delete_selected_color_correct == 'n':
            print()
            delete_selected_color = input('Which color do you want to delete?: ').lower()
            for i, item in enumerate(item_list):
                word = delete_selected_color + '-' + color_codes[i]
                if word == item:
                    word_with_color = '{}'.format(color_codes[i] + color_names[i].title() + "\x1b[0m")
            if delete_selected_color in color_names:
                sure_want_to_delete_color = 'n'
                while sure_want_to_delete_color == 'n':
                    print()
                    warning_message('Colors are not recoverable once deleted.')
                    want_to_delete_color = input(f'Are you sure you want to delete {word_with_color}? (y/n): ')
                    if want_to_delete_color == 'y':
                        remove_color_from_file(delete_selected_color)
                        print()
                        print(green('--SUCCESS:'), f'{word_with_color} has been deleted from {colored_file("saved_color_codes")}.')
                        print(f'You will be not be able to find your color anymore.')
                        input(light_purple('Press the Enter key to Continue. '))
                        make_the_sentence_again()
                    elif want_to_delete_color == 'n':
                        print()
                        warning_message('No color will be deleted.')
                        input(light_purple('Press the Enter key to Continue. '))
                        delete_selected_color_correct = 'y'
                        rgb_menu_sequence()
                    else:
                        print()
                        yn_typo_error(want_to_delete_color)
                        input(light_purple('Press the Enter key to Continue. '))
                        delete_selected_color = 'y'
            elif delete_selected_color == 'none':
                print()
                warning_message('No color was deleted.')
                input(light_purple('Press the Enter key to Continue. '))
                rgb_menu_sequence()
            elif delete_selected_color not in color_names:
                print()
                print(red('--TYPO ERROR:'), f'{possible_answer(delete_selected_color)} is an invalid command. Try typing in another command.')
                input(light_purple('Press the Enter key to Continue. '))
                delete_selected_color_correct = 'n'

def remove_color_from_file(color_to_delete):
    """
    deletes the color the user
    wants to delete from saved_color_codes.txt.

    Parameters:
    color_to_delete: the color the user wants to delete.
    
    Return: None.
    """
    with open('saved_color_codes.txt', 'rt') as scc_r:
        list_of_texts = []
        list_of_color_names = []
        list_of_color_codes = []
        for line in scc_r:
            list_of_texts.append(line.strip())
            name, code = line.split('-')
            list_of_color_names.append(name.strip())
            list_of_color_codes.append(code.strip())
    with open('saved_color_codes.txt', 'wt') as scc_w:
        scc_w.write('')
    with open('saved_color_codes.txt', 'at') as scc_a:
        for i, line in enumerate(list_of_texts):
            if line != color_to_delete + '-' + list_of_color_codes[i]:
                scc_a.write(f'{line}\n')

def main(): 
    """
    Asks the user what the sentence should be.

    Parameters:
    None

    Return: None.
    """
    # start of main
    print()
    # color choice error handling
    # asking the user which color they want the text to be
    setting_right = 'n'
    while setting_right == 'n':
        print(title_custom_color('Main Menu:'))
        print('---')
        tip(f'To view your color choices again, type {possible_answer("cc")} or {possible_answer("color choices")} in the field below.')
        tip(f'To view your action choices again, type {possible_answer("ac")} or {possible_answer("action choices")} in the field below.')
        tip(f'To see the contents of an existing file, type {possible_answer("pr")} or {possible_answer("print")} in the field below.')
        tip(f'To delete an existing sentence in a file, or an entire file, type {possible_answer("df")}, {possible_answer("delete file")}, {possible_answer("delete")}, or {possible_answer("d")} in the field below.')
        print('---')
        print()
        setting = input('Choose a color or an action: ').lower()
        if setting in ['red', 'r']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {red("red")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', red(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = red(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['yellow', 'y']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {yellow("yellow")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', yellow(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = yellow(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['green', 'g']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {green("green")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', green(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = green(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['light purple', 'lp']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {light_purple("light purple")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', light_purple(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = light_purple(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['purple', 'p']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {purple("purple")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', purple(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = purple(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['cyan', 'c', 'b', 'blue', 'cyan/blue']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {cyan("cyan/blue")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', cyan(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = cyan(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['light gray', 'lg', 'gray', 'white']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {light_gray("light gray")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', light_gray(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = light_gray(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['sr', 'easter egg', 'egg', 'hd', 'hidden in the depths']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                print(rainbow_words('<Kaden>'), rainbow_letters('You\'ve found my secret rainbow..'))
                input(light_purple('Press the Enter key to Continue. '))
                print()
                text_to_convert = input(f'What do you want the {secret_rainbow("secret rainbow")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', secret_rainbow(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = secret_rainbow(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['gray', 'g']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {gray("gray")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', gray(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = gray(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['rgb', 'custom']:
            rgb_menu_sequence()
        elif setting in ['rainbow words', 'rw']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {rainbow_words("rainbow words")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', rainbow_words(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = rainbow_words(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['rainbow letters', 'rl', 'cl', 'colorful letters']:
            text_to_convert_len_correct = 'n'
            while text_to_convert_len_correct == 'n':
                print()
                text_to_convert = input(f'What do you want the {rainbow_letters("rainbow letters")} text to say?: ')
                if len(text_to_convert) > 150:
                    print()
                    warning_message(f'Your sentence cannot be more than {yellow(150)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                elif len(text_to_convert) == 0:
                    print()
                    warning_message(f'Your sentence cannot be {yellow(0)} characters long. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    text_to_convert_len_correct = 'n'
                if text_to_convert == 'none':
                    print()
                    warning_message('Taking you back..')
                    input(light_purple('Press the Enter key to Continue. '))
                    main()
                if len(text_to_convert) < 150 and len(text_to_convert) > 0:
                    sentence_length = len(f'Your new colorized sentence is: {text_to_convert}')
                    print()
                    print('-' * sentence_length)
                    print(f'Your new colorized sentence is:', rainbow_letters(text_to_convert))
                    print('-' * sentence_length)
                    final_sentence = rainbow_letters(text_to_convert)
                    setting_right = 'y'
                    ssc(setting=setting, final_sentence=final_sentence)
        elif setting in ['cc', 'color choices']:
            color_choices()
            main()
        elif setting in ['ac', 'action choices']:
            action_choices()
            main()
        elif setting in ['df', 'delete file', 'delete', 'delete sentence', 'sentence', 'd']:
            delete_file_or_sentence()
        elif setting in ['print', 'pr']:
            list_of_texts = []
            with open('save_file.txt', 'rt') as fi:
                for i, line in enumerate(fi):
                    list_of_texts.append(line.strip())
            if len(list_of_texts) == 0:
                file_name = ''
                print_saved_sentences(file_name=file_name)
            elif len(list_of_texts) == 1:
                file_name = list_of_texts[0]
                print_saved_sentences(file_name=file_name)
                make_the_sentence_again()
            else:
                choice_of_text_correct = 'n'
                while choice_of_text_correct == 'n':
                    max_item_length = len(max(list_of_texts, key=len)) + 7
                    if len(list_of_texts) >= 1:
                        print()
                        print('Available text documents you can print:'.center(40))
                        print('-' * max_item_length)
                        for i, line in enumerate(list_of_texts):
                            if line != '\n':
                                print(f'{list_num_color(f"{i + 1}.")} {purple(f"{line.strip()}.txt")}')
                        print('-' * max_item_length)
                        tip(f'You can type {possible_answer("none")} in the field below to cancel this request.')
                        warning_message('You will need to type out the whole file name to access it.')
                        print()
                        tip(f'The {purple(".txt")} file extension will be applied automatically.')
                        choice_of_text = input(f'Which text document do you wish to see?: ').lower()
                        if choice_of_text in list_of_texts:
                            file_name = choice_of_text
                            choice_of_text_correct = 'y'
                            print_saved_sentences(file_name)   
                        elif choice_of_text == 'none':
                            print()
                            warning_message('No text file will be printed.')
                            input(light_purple('Press the Enter key to Continue. '))
                            make_the_sentence_again()
                        elif choice_of_text not in list_of_texts:
                            print()
                            print(red('--TYPO ERROR:'), f'{possible_answer(choice_of_text)} does not match any documents shown above. Try again.')
                            input(light_purple('Press the Enter key to Continue. '))
                            print()
                make_the_sentence_again()
        elif setting == 'none':
            print()
            warning_message('Quitting the program now..')
            input(light_purple('Press the Enter key to Continue. '))
            print()
            quit()
        elif setting in ['secret', 's', 'sc']:
            print()
            print(rainbow_words('<Kaden>'), rainbow_letters('There\'s a secret rainbow..'))
            input(light_purple('Press the Enter key to Continue. '))
            print()
            print(rainbow_words('<Kaden>'), rainbow_letters('Hidden in the Depths..'))
            input(light_purple('Press the Enter key to Continue. '))
            print()
            print(rainbow_words('<Kaden>'), rainbow_letters('You\'ve found the one and only easter egg.'))
            input(light_purple('Press the Enter key to Continue. '))
            setting_right = 'y'
            main()
        elif setting in ['new', 'n']:
            setting_right = 'y'
            new_file()
            make_the_sentence_again()
        elif setting in ['custom rainbow', 'cr']:
            custom_rainbow_menu()
            make_the_sentence_again()
        else:
            print()
            print(red('--TYPO ERROR:'), f'{possible_answer(setting)} is an invalid color choice. Try typing in another color choice.')
            input(light_purple('Press the Enter key to Continue. '))
            setting_right = 'n'
            print()

def make_the_sentence_again():
    """
    If you wish to end the program, this asks the user if they want to continue or end.

    Parameters:
    None.

    Return: None.
    """
    do_that_again_correct = 'y'
    while do_that_again_correct == 'y':
        print()
        tip(f'Typing {possible_answer("n")} in the field below quits the program.')
        do_that_again = input('Do you wish to return to the main menu? (y/n): ').lower()
        if do_that_again == 'y':
            main()
        elif do_that_again == 'n':
            print()
            print(red('--- © Kaden Hansen. All Rights Reserved. ---'))
            print()
            print(secret_rainbow('---'))
            print(secret_rainbow('I really enjoyed working on this project. I thank'))
            print(secret_rainbow('you for taking the time to run it. I definitely want'))
            print(secret_rainbow('to learn more about Python in the future.'))
            print(secret_rainbow('---'))
            print()
            quit()
        else:
            print()
            yn_typo_error(do_that_again)
            input(light_purple('Press the Enter key to Continue. '))

def save_sentence(file_name, sentence):
    """
    saves the given sentence to the save_file.txt file.

    Parameters:
    file_name: the name of the file is used to save the user's sentence to the document stated.
    (i. e. if my file was named colors.txt, the file_name would be 'colors'.)

    sentence: the user's sentence they'd like to save.
    
    Return: None.
    """
    with open(f'{file_name}.txt', 'at') as colored_sentences_file:
        colored_sentences_file.write(f'{sentence}\n')  
    file_accessed_()

def file_accessed_(number = 1):
    """
    the user can manually save a number to file_accessed_number.txt to tell the
    program if this is the first time the program is run.

    Parameters:
    number: the number that needs to be appended to the file.

    0 = first time ran

    1 = any other time ran (default)

    --Notice: The file does not apply the 0 automatically. The user must change the number
    in the file_accessed_number.txt file to have this effect anything.
    
    Return: None.
    """
    with open('file_accessed_number.txt', 'wt') as number_file:
        number_file.write(str(number))

def print_saved_sentences(file_name):
    """
    prints the saved sentences in a certain file when the user
    types 'pr' or 'print' as their color choice.

    Parameters:
    file_name: The name of the file the user wishes to see
    the contents of. 
    
    Return: None.
    """ 
    with open(f'{file_name}.txt', 'rt') as colored_sentences_file:
        items_list = []
        for item in colored_sentences_file:
            items_list.append(item)
    max_length = 0
    for sentence in items_list:
        pattern = re.compile(r'\x1b[^m]*m')
        clean_text = pattern.sub('', sentence.strip())
        length = len(clean_text)
        if length > max_length:
            max_length = length + 3
    if len(items_list) == 0:
        print(f'The sentences in {colored_file(f"{file_name}")} are:'.center(40))
        list_item_length = len(f'There are no sentences in {colored_file(f"{file_name}")}.') - 10
        print('-' * list_item_length)
        print(f'There are no sentences in {colored_file(f"{file_name}")}.')
        print('-' * list_item_length)
        tip(f'You only have {yellow("1")} text file in the CSP directory named {colored_file(file_name)}.')
        tip(f'You will need to add sentences to {colored_file(f"{file_name}")} to view them.')
        make_the_sentence_again()  
    elif len(items_list) >= 1:
        print()
        print(f'Your saved colorful sentences in {purple(f"{file_name}.txt")} are: ')
        print()
        print('-' * max_length)
        for i, line in enumerate(items_list):
            print(f'{list_num_color(f"{i + 1}.")} {line.strip()}')
        print('-' * max_length)
        colored_sentences_file.close()

def delete_file():
    """
    deletes a text file in this folder containing
    sentences if the user types 'df', 'delete file',
    'd', as their color choice.

    Parameters:
    None
    
    Return: None.
    """ 
    with open(f'save_file.txt', 'rt') as documents_file:
        items_list = []
        for item in documents_file:
            items_list.append(item.strip())
    max_item_length = len(max(items_list, key=len)) + 7
    if len(items_list) == 0:
        print()
        print(f'The documents you can delete are:'.center(40))
        print('-' * 40)
        print(f'There are no documents in {colored_file("save_file")}.')
        print('-' * 40)
        warning_message(f'You cannot delete files because {yellow("0")} exist.')
        tip(f'You will need to create text documents to delete them.')
        make_the_sentence_again()  
    elif len(items_list) == 1:
        print()
        print(f'The documents you can delete are:'.center(55))
        print('-' * 55)
        print(f'There are no documents you can delete in {colored_file("save_file")}.')
        print('-' * 55)
        warning_message(f'You cannot delete files because only {yellow("1")} exists.')
        tip(f'You will need to create more text documents to delete them.')
        make_the_sentence_again()  
    elif len(items_list) > 1:
        print()
        print(f'The documents you can delete are:')
        print()
        print('-' * max_item_length)
        for i, line in enumerate(items_list):
            print(f'{list_num_color(f"{i + 1}.")} {purple(f"{line.strip()}.txt")}')
        print('-' * max_item_length)
        tip(f'You can type {possible_answer("none")} in the field below to cancel this request.')
        warning_message('You will need to type out the whole file name to delete it.')
        delete_selected_file_correct = 'n'
        while delete_selected_file_correct == 'n':
            print()
            tip(f'The {purple(".txt")} file extension will be applied automatically.')
            delete_selected_file = input('Which file do you want to delete?: ').lower()
            if delete_selected_file in items_list:
                sure_want_to_delete_file = 'n'
                while sure_want_to_delete_file == 'n':
                    print()
                    print('---')
                    warning_message('Files are not recoverable once deleted.')
                    warning_message(f'If you delete all of your existing sentence files, (This would only be possible')
                    print(f'if done manually) you will need to change the {yellow("1")} in the {colored_file("file_accessed_number")} to {yellow("0")} so that the program doesn\'t crash.')
                    tip(f'(If you do this, be sure to save the {colored_file("file_accessed_number")} file before starting the program again)')
                    print('---')
                    print()
                    want_to_delete_file = input(f'Are you sure you want to delete {colored_file(f"{delete_selected_file}")}? (y/n): ')
                    if want_to_delete_file == 'y':
                        remove_file_contents(delete_selected_file)
                        remove_from_save_file(delete_selected_file)
                        os.remove(f'{delete_selected_file}.txt')
                        print()
                        print(green('--SUCCESS:'), f'{colored_file(f"{delete_selected_file}")} has been deleted.')
                        print(f'You will be not be able to find your file anymore.')
                        input(light_purple('Press the Enter key to Continue. '))
                        sure_want_to_delete_file = 'y'
                        make_the_sentence_again()
                    elif want_to_delete_file == 'n':
                        print()
                        warning_message('No file will be deleted.')
                        input(light_purple('Press the Enter key to Continue. '))
                        sure_want_to_delete_file = 'y'
                        delete_selected_file = 'y'
                        make_the_sentence_again()
                    else:
                        print()
                        yn_typo_error(want_to_delete_file)
                        input(light_purple('Press the Enter key to Continue. '))
                        sure_want_to_delete_file = 'n'
                        delete_selected_file = 'y'
            elif delete_selected_file == 'none':
                print()
                warning_message('No files were deleted.')
                input(light_purple('Press the Enter key to Continue. '))
                make_the_sentence_again()
            elif delete_selected_file not in items_list:
                print()
                print(red('--TYPO ERROR:'), f'{possible_answer(delete_selected_file)} is an invalid color choice. Try typing in another color choice.')
                input(light_purple('Press the Enter key to Continue. '))
                delete_selected_file = 'n'

def delete_file_or_sentence():
    """
    Asks the user if they'd like to delete the
    entire file or a sentence located in the file.

    Parameters:
    None

    Return: None.
    """
    delete_file_or_sentence_question_correct = 'n'
    while delete_file_or_sentence_question_correct == 'n':
        print()
        print(title_custom_color('Deletion Menu:'))
        print('---')
        tip(f'You can type either: {possible_answer("file")} or {possible_answer("f")} to delete an entire file, or type: {possible_answer("sentence from a file")}, {possible_answer("sentence")}, or {possible_answer("s")} to delete one sentence from a file in the field below.')
        tip(f'You can also type {possible_answer("none")} into the field below to cancel this request.')
        print('---')
        print()
        delete_file_or_sentence_question = input(f'Would you like to delete an entire {possible_answer("file")} or a {possible_answer("sentence from a file")}?: ').lower()
        if delete_file_or_sentence_question in ['file', 'f']:
            delete_file()
            delete_file_or_sentence_question_correct = 'y'
        elif delete_file_or_sentence_question == 'none':
            print()
            warning_message('The deletion action was canceled.')
            input(light_purple('Press the Enter key to Continue. '))
            make_the_sentence_again()
        elif delete_file_or_sentence_question in ['sentence', 'sentence from a file', 's']:
            setup_for_delete_sentence()
            delete_file_or_sentence_question_correct = 'y'
        else:
            print(red('--TYPO ERROR:'), f'{possible_answer(delete_file_or_sentence_question)} did not match the expected {possible_answer("file")}, {possible_answer("sentence from a file")}, or {possible_answer("sentence")}. Try again.')
            input(light_purple('Press the Enter key to Continue. '))

def setup_for_delete_sentence():
    """
    Shows a list of the user's saved text documents,
    so they can pick and choose what sentence they
    want deleted when delete_sentence() is called.
    

    Parameters:
    None

    Return: None.
    """
    print()
    with open('save_file.txt', 'rt') as fi:
        list_of_texts = []
        for i, line in enumerate(fi):
            list_of_texts.append(line.strip())
    print()
    if len(list_of_texts) == 0:
        print('Available text documents you can delete sentences from:'.center(51))
        print('-' * 51)
        print(f'There are no saved document names in {colored_file("save_file")}.'.center(51))
        print('-' * 51)
        tip(f'Make sure that the name of your {purple(".txt")} document is in {purple("save_file.txt")}.')
        make_the_sentence_again()
    else:
        max_length = 0
        for i, text in enumerate(list_of_texts):
            len_of_text = len(text)
            if len_of_text > max_length:
                max_length = len_of_text + 11
        document_choice_correct = 'n'
        while document_choice_correct == 'n':
            print('Available text documents you can delete sentences from:'.center(max_length))
            print('-' * max_length)
            for i, line in enumerate(list_of_texts):
                if line != '\n':
                    print(f'{list_num_color(f"{i + 1}.")} {purple((f"{line}.txt"))}')
            print('-' * max_length)
            tip(f'You can say {possible_answer("none")} in the field below to cancel this request.')
            warning_message('You will need to type out the whole file name to access it.')
            print()
            tip(f'The {purple(".txt")} file extension will be applied automatically.')
            document_choice = input('Which document do you wish to delete a sentence from?: ').lower()
            file_name = document_choice
            if file_name in list_of_texts:
                sure_want_to_delete_from_file_correct = 'n'
                while sure_want_to_delete_from_file_correct == 'n':
                    print()
                    sure_want_to_delete_from_file = input(f'Are you sure you want to delete a sentence from your {colored_file(f"{file_name}")} file? (y/n): ').lower()
                    if sure_want_to_delete_from_file == 'y':
                        delete_sentence(file_name)
                        document_choice_correct = 'y'
                        sure_want_to_delete_from_file_correct = 'y'
                    elif sure_want_to_delete_from_file == 'n':
                        sure_want_to_delete_from_file_correct = 'y'
            elif file_name not in list_of_texts:
                print()
                print(red('--TYPO ERROR:'), f'{possible_answer(f"{document_choice}.txt")} does not match any documents shown above. Try again.')
                input(light_purple('Press the Enter key to Continue. '))
                print()
            if document_choice == 'none':
                print()
                warning_message('No sentences will be deleted.')
                input(light_purple('Press the Enter key to Continue. '))
                make_the_sentence_again()

def delete_sentence(file_name):
    """
    Opens a text document, showing the user the
    text inside. They can then choose which sentence
    to delete by number.

    Parameters
    file_name: The file name of the file the sentence needs
    to be deleted from.

    Return: None.
    """
    with open(f'{file_name}.txt', 'rt') as selected_file:
        list_of_texts = []
        list_of_numbers = []
        for i, sentence in enumerate(selected_file):
            list_of_texts.append(sentence.strip())
            list_of_numbers.append(str(i + 1))
    max_length = 0
    for i, sentence in enumerate(list_of_texts):
        pattern = re.compile(r'\x1b[^m]*m')
        clean_text = pattern.sub('', sentence)
        length = len(clean_text)
        if length > max_length:
            max_length = length + 3
    sentence_to_delete_correct = 'n'
    while sentence_to_delete_correct == 'n':
        print()
        if len(list_of_texts) == 0:
            list_item_length = len(f'There are no sentences in {colored_file(f"{file_name}")}.')
            print(f'Available sentences you can delete in {colored_file(f"{file_name}")}:'.center(list_item_length))
            print('-' * list_item_length)
            print(f'There are no sentences in {colored_file(f"{file_name}")}.'.center(52))
            print('-' * list_item_length)
            tip(f'You will need to add sentences to {colored_file(f"{file_name}")} to delete them.')
            make_the_sentence_again()

        else:
            print(f'Available sentences you can delete in {colored_file(f"{file_name}")}:'.center(max_length))
            print('-' * max_length)
            for i, sentence in enumerate(list_of_texts):
                if sentence != '\n':
                    print(f'{list_num_color(f"{i + 1}.")} {sentence}')
            print('-' * max_length)
            tip(f'You can type {possible_answer("none")} in the field below to cancel this request.')
            print()
            tip('To delete a certain sentence, type in its corresponding number in the field below.')
            sentence_to_delete = input(f'Which sentence in {colored_file(f"{file_name}")} do you wish to delete?: ').lower()
            if sentence_to_delete == 'none':
                sentence_to_delete_correct = 'y'
                print()
                warning_message(f'No sentences will be deleted from {colored_file(file_name)}.')
                input(light_purple('Press the Enter key to Continue. '))
                make_the_sentence_again()
            try:
                sentence_to_delete = int(sentence_to_delete)
                if str(sentence_to_delete) in list_of_numbers:
                    sentence_to_delete_correct = 'y'
                    with open(f'{file_name}.txt', 'rt') as f_read:
                        list_of_sentences = []
                        for line in f_read:
                            list_of_sentences.append(line.strip())
                    sure_delete_sentence_correct = 'n'
                    while sure_delete_sentence_correct == 'n':
                        print()
                        sure_delete_sentence = input(f'Are you sure you want to delete sentence {yellow(f"{sentence_to_delete}")} from {colored_file(f"{file_name}")}? (y/n): ')
                        if sure_delete_sentence == 'y':
                            with open(f'{file_name}.txt', 'wt') as f_write:
                                f_write.write('')
                                for i, _ in enumerate(list_of_sentences):
                                    if i + 1 != sentence_to_delete:
                                        f_write.write(f'{list_of_sentences[i]}\n')
                            print()
                            print(green('--SUCCESS:'), f'Sentence {yellow(sentence_to_delete)} has been deleted from {colored_file(f"{file_name}")}.')
                            print('You will not be able to find it anymore.')
                            input(light_purple('Press the Enter key to Continue. '))
                            make_the_sentence_again()
                        elif sure_delete_sentence == 'n':
                            print()
                            warning_message(f'Sentence {yellow(f"{sentence_to_delete}")} will not be deleted from {colored_file(f"{file_name}")}.')
                            input(light_purple('Press the Enter key to Continue. '))
                            make_the_sentence_again()
                        else:
                            print()
                            yn_typo_error(sure_delete_sentence)
                            input(light_purple('Press the Enter key to Continue. '))
                else:
                    print()
                    print(red('--VALUE ERROR:'), f'sentence {possible_answer(sentence_to_delete)} doesn\'t exist. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
            except ValueError:
                print()
                print(red('--VALUE ERROR:'), f'{possible_answer(sentence_to_delete)} is not a number. Try again.')
                input(light_purple('Press the Enter key to Continue. '))

def remove_file_contents(file_name):
    """
    Removes all of text in the wanting-to-delete
    file so that the file can be deleted.

    Parameters:
    file_name: The name of the file that needs
    to have it's contents erased.
    
    Return: None.
    """
    with open(f'{file_name}.txt', 'wt') as f:
        f.write('')

def remove_from_save_file(file_to_delete):
    """
    deletes the file name of the file the user
    wants to delete from save_file.txt so the
    program won't crash.

    Parameters:
    file_to_delete: the file the user wants to delete
    
    Return: None.
    """
    with open('save_file.txt', 'rt') as f_read:
        list_of_texts = []
        for line in f_read:
            list_of_texts.append(line.strip())
    with open('save_file.txt', 'wt') as f_write:
        for i, document in enumerate(list_of_texts):
            if document != file_to_delete:
                f_write.write(f'{list_of_texts[i]}\n')

def save_file(file_name):
    """
    saves all of the created file names to one file called save_file.txt
    to have the program pull the needed information from that file using
    the names in save_file.txt.

    (i. e. if I had a file called colors.txt, save_file.txt would receive
    'colors' as reference to the colors.txt. The program can then pull
    from save_file to do necessary tasks)

    Parameters:
    file_name: the name of the file to append to save_file.txt
    
    Return: None.
    """
    with open('save_file.txt', 'at') as f:
        f.write(f'\n{file_name}')

def create_new_file_q(final_sentence):
    """
    Allows the user to create a new file to save sentences in.

    Parameters:
    final_sentence: the sentence the user wants to add to this new file.
    
    Return: None.
    """
    make_new_file_correct = 'n'
    while make_new_file_correct == 'n':
        make_new_file = input('Would you like to make a new file? (y/n): ').lower()
        if make_new_file == 'y':
            file_name_correct = 'n'
            while file_name_correct == 'n':
                print()
                tip(f'the {purple(".txt")} file extension will be applied automatically.')
                file_name = input('What would you like to call this file?: ').lower()
                # file_name user error handling
                invalid_character_counter = 0
                valid_character_count = 0
                file_name_correct = 'y'
                invalid_character_list = [ '/', '\\', '<', '>', '|', '?', ':', '*', '.']
                # checking if any character in the string is an invalid one
                # If there are, the name doesn't pass
                for letter in file_name:
                    for character in invalid_character_list:
                        if letter == character:
                            invalid_character = character
                            print()
                            print(red('--TYPO ERROR:'), f'your file name cannot contain a {possible_answer(f"{invalid_character}")}. Try again.')
                            input(light_purple('Press the Enter key to Continue. '))
                            invalid_character_counter += 1
                        elif letter != character:
                            valid_character_count += 1
                        if invalid_character_counter > 0:
                            file_name_correct = 'n'  
                        # end of file_name_error_handling
                # do only if string has no invalid characters
                if invalid_character_counter == 0:
                    # final_file_correct error handling
                    with open('save_file.txt', 'rt') as sf_read:
                        lines = sf_read.readlines()
                    for line in lines:
                        cleanline = line.strip()
                        if cleanline == file_name:
                            file_name_correct = 'n'
                            print()
                            print(red('Error:'), f'{colored_file(file_name)} already exists. Try again.')
                            input(light_purple('Press the Enter key to Continue. '))
                            break
                        else:
                            file_name_correct = 'y'
                    if file_name_correct != 'n':
                        file_compare = f'{file_name}.txt'
                        files = os.listdir(".")
                        for filename in files:
                            if file_compare == filename:
                                file_name_correct = 'n'
                                print()
                                print(red('Error:'), f'{colored_file(file_name)} already exists. Try again.')
                                input(light_purple('Press the Enter key to Continue. '))
                                break
                            else:
                                file_name_correct = 'y'
                    if file_name_correct == 'y':
                        final_file_correct1 = 0
                        while final_file_correct1 == 0:
                            print()
                            tip(f'You can type {possible_answer(f"none")} in the field below to cancel this request.')
                            final_file = input(f'Are you sure you want to call your file {colored_file(file_name)}? (y/n): ').lower()
                            if final_file == 'none':
                                print() 
                                warning_message('No file will be created.') 
                                input(light_purple('Press the Enter key to Continue. '))
                                print()
                                make_the_sentence_again()
                            elif final_file == 'y':
                                save_sentence(file_name=file_name, sentence=final_sentence)
                                save_file(file_name=file_name)
                                print()
                                print(green('--SUCCESS:'), f'Your sentence has been saved in', colored_file(file_name) + '.')
                                print(f'You will be able to find your file in the folder with both program files.')
                                input(light_purple('Press the Enter key to Continue. '))
                                print()
                                tip('You can access your saved sentences even when the program stops running. Go to the instructions for more info.')
                                input(light_purple('Press the Enter key to Continue. '))
                                file_accessed_()
                                final_file_correct1 = 1
                                file_name_correct = 'y'
                                make_the_sentence_again()
                            elif final_file == 'n':
                                file_name_correct = 'n'
                                final_file_correct1 = 1
                            else:
                                print()
                                yn_typo_error(final_file)
                                input(light_purple('Press the Enter key to Continue. '))
                    else:
                        print()
                        warning_message(f'Because an error has occurred, you\'ll need to confirm')
                        print('that you want to create a new file again. If you don\'t want')
                        print(f'to create a new file, please type {possible_answer("n")}.')
                        
                        input(light_purple('Press the Enter key to Continue. '))
                        print()
                        create_new_file_q(final_sentence=final_sentence)
        elif make_new_file == 'n':
            discard_correct = 'n'
            while discard_correct == 'n':
                wish_to_continue_correct = 'n'
                while wish_to_continue_correct == 'n':
                    print()
                    warning_message('You are about to discard this sentence.')
                    wish_to_continue = input('Are you sure you don\'t want to save this sentence? (y/n): ').lower()
                    if wish_to_continue == 'y':
                        wish_to_continue_correct = 'y'
                        print()
                        warning_message('Your sentence has not been saved.')
                        input(light_purple('Press the Enter key to Continue. '))
                        make_the_sentence_again()
                    elif wish_to_continue == 'n':
                        file_name = 'first'
                        wish_to_continue_correct = 'y'
                        save_sentence(file_name=file_name, sentence=final_sentence)
                        print()
                        print(green('--AUTO SAVE:'), f'Because you weren\'t sure about deleting your sentence,')
                        print(f'it has been backed up to {colored_file(file_name)}. You can find it in this program\'s main folder.')
                        input(light_purple('Press the Enter key to Continue. '))
                        print()
                        tip('You can access your saved sentences even when the program stops running. Go to the instructions for more info.')
                        input(light_purple('Press the Enter key to Continue. '))
                        make_the_sentence_again()
                    else:
                        print()
                        yn_typo_error(wish_to_continue)
                        input(light_purple('Press the Enter key to Continue. '))
        else:
            print()
            yn_typo_error(make_new_file)
            input(light_purple('Press the Enter key to Continue. '))

def new_file():
    """
    Creates a new file that
    a user can add sentences to.

    Parameters: None.

    Return: None.
    """

    file_name_correct = 'n'
    while file_name_correct == 'n':
        print()
        print(title_custom_color("New Document:"))
        print('---')
        tip(f'the {purple(".txt")} file extension will be applied automatically.')
        file_name = input('What would you like to call this new file?: ').lower()
        if file_name == 'none':
            print() 
            warning_message('No file will be created.') 
            input(light_purple('Press the Enter key to Continue. '))
            make_the_sentence_again()
        # file_name user error handling
        invalid_character_counter = 0
        valid_character_count = 0
        file_name_correct = 'y'
        invalid_character_list = [ '/', '\\', '<', '>', '|', '?', ':', '*', '.']
        # checking if any character in the string is an invalid one
        # If there are, the name doesn't pass
        for letter in file_name:
            for character in invalid_character_list:
                if letter == character:
                    invalid_character = character
                    print()
                    print(red('--TYPO ERROR:'), f'your file name cannot contain a {possible_answer(f"{invalid_character}")}. Try again.')
                    input(light_purple('Press the Enter key to Continue. '))
                    invalid_character_counter += 1
                elif letter != character:
                    valid_character_count += 1
                if invalid_character_counter > 0:
                        file_name_correct = 'n'  
            # end of file_name_error_handling
            # do only if string has no invalid characters
            if invalid_character_counter == 0:
                # final_file_correct error handling
                final_file_correct1 = 0
                while final_file_correct1 == 0:
                    print()
                    tip(f'You can type {possible_answer(f"none")} in the field below to cancel this request.')
                    final_file = input(f'Are you sure you want to call your file {colored_file(file_name)}? (y/n): ').lower()
                    if final_file == 'none':
                        print() 
                        warning_message('No file will be created.') 
                        input(light_purple('Press the Enter key to Continue. '))
                        print()
                        make_the_sentence_again()
                    elif final_file == 'y':
                        final_file_correct1 = 1
                        save_file(file_name=file_name)
                        make_new_file(file_name=file_name, )
                        print()
                        print(green('--SUCCESS:'), f'Your sentence has been saved in', colored_file(file_name) + '.')
                        print(f'You will be able to find your file in the folder with both program files.')
                        input(light_purple('Press the Enter key to Continue. '))
                        file_accessed_()
                        make_the_sentence_again()
                    elif final_file == 'n':
                        final_file_correct1 = 1
                        new_file()
                        make_the_sentence_again()
                    else:
                        print()
                        yn_typo_error(final_file)

def make_new_file(file_name):
    """
    Makes the new file in the CSP Directory.

    Parameters:
    filename: The filename the user wants to name the new text file.
    final_sentence: The sentence that the user made. (This is here
    so that if they try to write a file that already exists, they'll
    have to try and save their sentence again.)

    Return: (potential) if the file exists or not.
    """
    with open(file_name, 'wt') as colored_sentences_file:
        colored_sentences_file.write('')
    file_accessed_()

if __name__ == '__main__':
    begin_error_check()
    instruction_introduction()
    main()