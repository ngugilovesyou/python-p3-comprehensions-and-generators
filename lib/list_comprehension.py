#!/usr/bin/env python3

def return_evens(num_list):
    show_even = [num for num in num_list if num%2 == 0 ]
    return show_even
    

def make_exclamation(sentence_list):
    exclamate_sentence = [sentence + "!" for sentence in sentence_list]
    return exclamate_sentence