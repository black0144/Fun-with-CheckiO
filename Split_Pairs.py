#!/usr/bin/env python
# -*- coding:utf-8 -*-

def split_pairs(a):
  '''
  a+='_'*(len(a)%2)
  return [a[i:i+2] for i in range(0,len(a),2)]
  '''
  '''
  N = len(a)
  if N % 2 == 1: a += "_"
  return [a[i:i+2] for i in range(0,N,2)]
  '''
  return [(a[i:i+2]+'_')[:2] for i in range(0, len(a), 2)]
  
if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcde')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")