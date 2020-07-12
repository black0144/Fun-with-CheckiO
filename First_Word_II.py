#!/usr/bin/env python
# -*- coding:utf-8 -*-

def first_word(text: str) -> str:

    result=[]
    text=(text.replace("."," ")).replace(","," ")
    for word in text.split():
        result.append(word)
    return result[0]
    '''
    res = ''
    for ch in text.lstrip(" .,'"):
        if ch.isalpha() or ch == "'":
            res += ch
        else:
            break
    return res
    '''
    #return text.replace('.', ' ').replace(',', ' ').split()[0]
    


if __name__ == '__main__':
    print("Example:")
    print(first_word(" a word "))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")