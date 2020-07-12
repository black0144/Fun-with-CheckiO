#!/usr/bin/env python
# -*- coding:utf-8 -*-

def is_all_upper(text: str) -> bool:
  #return text.isupper() or text.strip() == "" or text.isnumeric()
  return text.upper() == text
    
if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('123'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")


