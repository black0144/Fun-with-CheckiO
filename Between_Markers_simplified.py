#!/usr/bin/env python
# -*- coding:utf-8 -*-


def between_markers(text: str, begin: str, end: str) -> str:
  #return text[text.find(begin)+1:text.find(end)]
  return (text.split(begin))[1].split(end)[0]
    
    

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is [apple]', '[', ']'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')