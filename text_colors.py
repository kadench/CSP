"""
\x1b is the escape character (ASCII code 27) that starts all ANSI escape codes.
38 is the code for foreground color.
2 is the code for 24-bit RGB color mode.
254;217;183 are the RGB values for the color, in decimal format.
m indicates the end of the ANSI escape code.

Result:
\x1b[38;2;128;128;128m
"""
import re

def red(text):
    """
    Changes the color of the text to red.

    Parameters:
    text: text to convert
    
    Return: red text
    """
    red_color = '\x1b[91m{}\x1b[00m'.format(text)
    return red_color

def yellow(text):
    """
    Changes the color of the text to yellow.

    Parameters:
    text: text to convert
    
    Return: yellow text
    """
    yellow_color = '\x1b[93m{}\x1b[00m'.format(text)
    return yellow_color

def green(text):
    """
    Changes the color of the text to green.

    Parameters:
    text: text to convert
    
    Return: green text
    """
    color_green = '\x1b[92m{}\x1b[00m'.format(text)
    return color_green

def cyan(text):
    """
    Changes the color of the text to cyan.

    Parameters:
    text: text to convert
    
    Return: cyan text
    """
    cyan_color = '\x1b[96m{}\x1b[00m'.format(text)
    return cyan_color

def light_purple(text):
    """
    Changes the color of the text to light purple.

    Parameters:
    text: text to convert
    
    Return: light purple text
    """
    light_purple_color = '\x1b[94m{}\x1b[00m'.format(text)
    return light_purple_color

def purple(text):
    """
    Changes the color of the text to purple.

    Parameters:
    text: text to convert
    
    Return: purple text
    """
    purple_color = '\x1b[95m{}\x1b[00m'.format(text)
    return purple_color

def light_gray(text): 
    """
    Changes the color of the text to light gray.

    Parameters:
    text: text to convert
    
    Return: light gray text
    """

    light_gray_color = '\x1b[97m{}\x1b[00m'.format(text)
    return light_gray_color

def gray(text):
    """
    Changes the color of the text to gray.

    Parameters:
    text: text to convert
    
    Return: gray text
    """

    gray_color = '\x1b[98m{}\x1b[00m'.format(text)
    return gray_color

def rainbow_letters(text):
    """
    Colors the letters in the text one by one in the repeating colors: 
    red, yellow, green, cyan, light purple, purple, white.

    Parameters:
    text: text to convert
    
    Return: rainbow text for every letter in the text
    """
    # define colors
    colors = [
        '\x1b[91m',  # red
        '\x1b[93m',  # yellow
        '\x1b[92m',  # green
        '\x1b[96m',  # cyan
        '\x1b[94m',  # light purple
        '\x1b[95m',  # purple
        '\x1b[97m'   # white
    ]

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

def rainbow_words(text):
    """
    Colors the words one by one in the text provided in these 
    repeating colors: red, yellow, green, cyan, light purple,
    purple, white.

    Parameters:
    text: text to convert
    
    Return: rainbow text by word
    """
    # define colors
    colors = [
        '\x1b[91m',  # red
        '\x1b[93m',  # yellow
        '\x1b[92m',  # green
        '\x1b[96m',  # cyan
        '\x1b[94m',  # light purple
        '\x1b[95m',  # purple
        '\x1b[97m'   # white
    ]

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

def secret_rainbow(text):
    """
    Colors the letters in each word one by one in the text provided 
    in a repeating color scheme: magenta dye, Steel blue, Hunyadi yellow,
    Persian green, Flax, Orange (Crayola) and Dark Purple

    Parameters:
    text: text to convert
    
    Return: colorful text for every letter in every word
    """
    # define colors
    colors = [
        '\x1b[38;2;186;44;115m',  # magenta dye
        '\x1b[38;2;45;125;210m',  # steel blue
        '\x1b[38;2;221;164;72m',  # hunyadi yellow
        '\x1b[38;2;27;153;139m',  # persian green
        '\x1b[38;2;227;217;133m',  # flax
        '\x1b[38;2;229;122;68m',  # crayola orange
        '\x1b[38;2;66;32;64m'   # dark purple
    ]

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

    # combine colored letters into the final secret rainbow
    # string
    secret_rainbow_string = ''.join(rainbow_letter_list)

    # resets text color to default
    secret_rainbow_string += '\x1b[0m'

    # return the rainbow string
    return secret_rainbow_string

def main():
    """
    Gives a message to the user, telling them
    that they cannot run this file and expect
    an output. 

    (Do not import main() into your
    own document as this file's main will add to
    yours if you have one.)

    Parameters:
    None

    Return: nothing
    """
    print(f"{purple('text_colors.py')} is not a program you should run. Instead,")
    print(f"it is a library of functions {purple('colored_sentence_maker.py')}")
    print("uses to color the sentences while the user uses the program.")
    print()
    print("To use these functions in your own python files, first, move this")
    print("file into the same folder/directory as the python file you want to use")
    print("these functions with. Then, import this file into your python file with")
    print("this statement:")
    print()
    print(f"{purple('from')} text_colors {purple('import *')}")
    print()

if __name__ == "__main__":
    main()