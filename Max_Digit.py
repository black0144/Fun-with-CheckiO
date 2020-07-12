#!/usr/bin/env python
# -*- coding:utf-8 -*-

def max_digit(number: int) -> int:
    '''
    j=str(number)[0]
    for i in str(number):
      if i>j:
        j=i
    return int(j)
    '''
    #return max(int(i) for i in str(number))
    #return max([int(i) for i in str(number)])
    #return int(max(list(str(number))))
    return int(max(str(number)))

if __name__ == '__main__':
    print("Example:")
    print(max_digit(52))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")