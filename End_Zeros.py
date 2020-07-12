#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

def end_zeros(num: int) -> int:
    '''
    matchObj = re.search( r'0*$', str(num), re.M|re.I) 
    if matchObj:
        return len(matchObj.group())
    '''

    '''
    return len(str(num)) - len(str(num).rstrip('0'))
    '''

    matchObj = re.search('0*$',str(num))
    return len(matchObj.group())

if __name__ == '__main__':
    print("Example:")
    print(end_zeros(10200))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
