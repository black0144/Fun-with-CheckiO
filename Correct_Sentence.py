#!/usr/bin/env python
# -*- coding:utf-8 -*-

def correct_sentence(text: str) -> str:
    '''
    first = text[0].upper()
    if text[-1] != '.':
      return first+text[1:]+'.'
    else:
      return first+text[1:]
    '''
    '''
    t=text[0].upper()+text[1:]
    if(t[-1]!='.'):
        t=t+'.'
    return t
    '''
    return text[0].upper() + text[1:] + '.' * (text[-1] != '.')



if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
