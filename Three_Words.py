#!/usr/bin/env python
# -*- coding:utf-8 -*-

def checkio(words: str) -> bool:
    '''
    tmp = []
    for word in words.split(' '):
        if word.isalpha():
            tmp.append(word)
            if len(tmp) == 3:
                return True
        else:
            tmp = []
    return False
    '''
    count_word = 0
    for word in words.split():
        if word.isdigit():
            count_word = 0
        else:
            count_word += 1
        if count_word == 3:
            return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("1 1 1 1"))
    

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")