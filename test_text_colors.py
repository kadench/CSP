import pytest
from text_colors import *

# text_color.py test functions:

def test_red():
    """
    Test if red() function returns red
    text every time it's used

    Parameters:
    None.

    Return: None.
    """
    # Test assertion 1: Pass text into the red() function to make sure the text is red.
    text = 'egg'
    converted_text = red(text=text)

    # assert that the returned text is red.
    assert converted_text == '\x1b[91m{}\x1b[00m'.format(text)

def test_yellow():
    """
    Test if yellow() function returns yellow
    text every time it's used

    Parameters:
    None.

    Return: None.
    """
    # Test assertion 1: Pass text into the yellow() function to make sure the text is yellow.
    text = 'egg'
    converted_text = yellow(text=text)

    # assert that the returned text is yellow.
    assert converted_text == '\x1b[93m{}\x1b[00m'.format(text)

def test_green():
    """
    Test if green() function returns green
    text every time it's used

    Parameters:
    None.

    Return: None.
    """
    # Test assertion 1: Pass text into the green() function to make sure the text is green.
    text = 'jello'
    converted_text = green(text)

    # # assert that the returned text is green.
    assert converted_text == '\x1b[92m{}\x1b[00m'.format(text)
   
def test_cyan():
    """
    Test if cyan() function returns cyan
    text every time it's used

    Parameters:
    None.

    Return: None.
    """
    # Test assertion 1: Pass text into the cyan() function to make sure the text is cyan.
    text = 'ocean'
    converted_text = cyan(text)

    # assert that the returned text is cyan.
    assert converted_text == '\x1b[96m{}\x1b[00m'.format(text)

def test_light_purple():
    """
    Test if light_purple() function returns light purple
    text every time it's used

    Parameters:
    None.

    Return: None.
    """
    # Test assertion 1: Pass text into the light_purple() function to make sure the text is light purple.
    text = 'grape'
    converted_text = light_purple(text)

    # assert that the returned text is light purple.
    assert converted_text == '\x1b[94m{}\x1b[00m'.format(text)

def test_purple():
    """
    Test if purple() function returns purple
    text every time it's used

    Parameters:
    None.

    Return: None.
    """
    # Test assertion 1: Pass text into the purple() function to make sure the text is purple.
    text = 'lavender'
    converted_text = purple(text)

    # assert that the returned text is purple.
    assert converted_text == '\x1b[95m{}\x1b[00m'.format(text)

def test_light_gray():
    """
    Test if light_gray() function returns light gray
    text every time it's used

    Parameters:
    None.

    Return: None.
    """
    # Test assertion 1: Pass text into the light_gray() function to make sure the text is light gray.
    text = 'cloud'
    converted_text = light_gray(text)

    # assert that the returned text is light gray.
    assert converted_text == '\x1b[97m{}\x1b[00m'.format(text)

def test_gray():
    """
    Test if gray() function returns gray
    text every time it's used

    Parameters:
    None.

    Return: None.
    """
    # Test assertion 1: Pass text into the gray() function to make sure the text is gray.
    text = 'elephant'
    converted_text = gray(text)

    # assert that the returned text is gray.
    assert converted_text == '\x1b[98m{}\x1b[00m'.format(text)

def test_rainbow_letters():
    # define an input to put into rainbow_word()
    input_str = 'abjectednesses'

    # Test assertion 1: makes sure the rainbow_letters() return of the inputted text is the expected rainbow string.
    # The expected string is hand-made to make sure the function gives the same result.
    expected_str = '\x1b[91ma\x1b[93mb\x1b[92mj\x1b[96me\x1b[94mc\x1b[95mt\x1b[97me\x1b[91md\x1b[93mn\x1b[92me\x1b[96ms\x1b[94ms\x1b[95me\x1b[97ms\x1b[0m'
    assert rainbow_letters(input_str) == expected_str

    # Test assertion 2: makes sure the string returned always equals the expected
    # amount of characters or y up to the max allowed characters in a string (150)
    # in my program.
    # 0 characters in the inputted string should = 4 in the return.
    # 1 character in the inputted string should = 10 in the return.
    # 2 characters in the inputted string should = 16 in the return.
    # etc.
    for x in range(150):
        input_str = 'a' * x
        y = 6 * x + 4
        assert len(rainbow_letters(input_str)) == y

def test_rainbow_words():
    # Test assertion 1: makes sure the rainbow_words() return of the inputted text is the expected rainbow string.
    # The expected string is hand-made to make sure the function gives the same result.
    input_text = "This is a test sentence"
    expected_str = '\x1b[91mThis \x1b[93mis \x1b[92ma \x1b[96mtest \x1b[94msentence\x1b[0m'
    assert rainbow_words(input_text) == expected_str

    # Test assertion 2: makes sure the string returned always equals the expected
    # amount of characters of each value in expected_character_counts (expected
    # string lengths after function run) up to the max allowed characters in a string
    # (150) in my program.

    # 0 characters in the inputted string should = 4 in the return.
    # 1 character in the inputted string should = 11 in the return.
    # 2 characters in the inputted string should = 18 in the return.
    # etc.
    expected_character_counts = [4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88, 95,
                                 102, 109, 116, 123, 130, 137, 144, 151, 158, 165, 172,
                                 179, 186, 193, 200, 207, 214, 221, 228, 235, 242, 249,
                                 256, 263, 270, 277, 284, 291, 298, 305, 312, 319, 326,
                                 333, 340, 347, 354, 361, 368, 375, 382, 389, 396, 403,
                                 410, 417, 424, 431, 438, 445, 452, 459, 466, 473, 480,
                                 487, 494, 501, 508, 515, 522, 529, 536, 543, 550, 557,
                                 564, 571, 578, 585, 592, 599, 606, 613, 620, 627, 634,
                                 641, 648, 655, 662, 669, 676, 683, 690, 697, 704, 711,
                                 718, 725, 732, 739, 746, 753, 760, 767, 774, 781, 788,
                                 795, 802, 809, 816, 823, 830, 837, 844, 851, 858, 865,
                                 872, 879, 886, 893, 900, 907, 914, 921, 928, 935, 942,
                                 949, 956, 963, 970, 977, 984, 991, 998, 1005, 1012,
                                 1019, 1026, 1033, 1040, 1047]
    for x in range(150):
        input_str = 'a ' * x
        expected_count = expected_character_counts[x]
        assert len(rainbow_words(input_str)) == expected_count

def test_secret_rainbow():
    # define an input to put into secret_rainbow()
    input_str = 'abjectednesses'

    # Test to see if the secret_rainbow_letters() return of the made up colored word 'abjectednesses' equals the manual-made secret rainbow string of that word.
    expected_str = '\x1b[38;2;186;44;115ma\x1b[38;2;45;125;210mb\x1b[38;2;221;164;72mj\x1b[38;2;27;153;139me\x1b[38;2;227;217;133mc\x1b[38;2;229;122;68mt\x1b[38;2;66;32;64me\x1b[38;2;186;44;115md\x1b[38;2;45;125;210mn\x1b[38;2;221;164;72me\x1b[38;2;27;153;139ms\x1b[38;2;227;217;133ms\x1b[38;2;229;122;68me\x1b[38;2;66;32;64ms\x1b[0m'
    assert secret_rainbow(input_str) == expected_str

    # Test assertion 2: makes sure the string returned always equals the expected
    # amount of characters in the expected_character_list up to the max allowed
    # characters in a string (150) in my program.
    # 0 characters in the inputted string should = 4 in the return.
    # 1 character in the inputted string should = 23 in the return.
    # 2 characters in the inputted string should = 42 in the return.
    # etc.
    expected_character_counts = [4, 23, 42, 61, 80, 100, 119, 136, 155, 174, 193, 212, 232, 251,
                                 268, 287, 306, 325, 344, 364, 383, 400, 419, 438, 457, 476, 496,
                                 515, 532, 551, 570, 589, 608, 628, 647, 664, 683, 702, 721, 740,
                                 760, 779, 796, 815, 834, 853, 872, 892, 911, 928, 947, 966, 985,
                                 1004, 1024, 1043, 1060, 1079, 1098, 1117, 1136, 1156, 1175, 1192,
                                 1211, 1230, 1249, 1268, 1288, 1307, 1324, 1343, 1362, 1381, 1400,
                                 1420, 1439, 1456, 1475, 1494, 1513, 1532, 1552, 1571, 1588, 1607,
                                 1626, 1645, 1664, 1684, 1703, 1720, 1739, 1758, 1777, 1796, 1816,
                                 1835, 1852, 1871, 1890, 1909, 1928, 1948, 1967, 1984, 2003, 2022,
                                 2041, 2060, 2080, 2099, 2116, 2135, 2154, 2173, 2192, 2212, 2231,
                                 2248, 2267, 2286, 2305, 2324, 2344, 2363, 2380, 2399, 2418, 2437,
                                 2456, 2476, 2495, 2512, 2531, 2550, 2569, 2588, 2608, 2627, 2644,
                                 2663, 2682, 2701, 2720, 2740, 2759, 2776, 2795, 2814]
    for x in range(150):
        input_str = 'a' * x
        expected_count = expected_character_counts[x]
        assert len(secret_rainbow(input_str)) == expected_count

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])