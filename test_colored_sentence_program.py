"""
I couldn't find out how to test any of my functions
in the main CSP program because they either open a file
or require lots of imput. I couldn't wrap my head around
how to test these functions. I found some examples that
talked about using Python's unittest module, but other
sources said that the module is very hard to learn.
I worked really hard to test my color functions in
test_text_colors.py, so hopefully that'll be enough.
"""

import pytest
from colored_sentence_program import *

def test_ask_to_save_color_code():
    pass

def test_begin_error_check():
    pass

def test_check_if_file_has_been_accessed():
    pass

def test_color_choices():
    pass

def test_colored_file():
    pass

def test_create_new_file_q():
    pass

def test_custom_color_applier():
    pass

def test_custom_color_maker():
    pass

def test_delete_file():
    pass

def test_delete_file_or_sentence():
    pass

def test_delete_saved_color():
    pass

def test_delete_sentence():
    pass

def test_file_accessed_():
    pass

def test_instruction_introduction():
    pass

def test_instructions():
    pass

def test_list_num_color():
    pass

def test_main():
    pass

def test_make_the_sentence_again():
    pass

def test_pick_from_saved_colors():
    pass

def test_possible_answer():
    pass

def test_print_saved_colors():
    pass

def test_print_saved_sentences():
    pass

def test_remove_color_from_file():
    pass

def test_remove_file_contents():
    pass

def test_remove_from_save_file():
    pass

def test_save_color_code():
    pass

def test_save_file():
    pass

def test_save_sentence():
    pass

def test_save_sentence_sequence():
    pass

def test_sentence_color_example():
    pass

def test_setup_for_delete_sentence():
    pass

def test_ssc():
    pass

def test_tip():
    pass

def test_title_custom_color():
    pass

def test_use_color():
    pass

def test_warning_message():
    pass

def test_yn_typo_error():
    pass

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])