#!/usr/bin/env python
# -*- coding:utf-8 -*-

def nearest_value(values: set, one: int) -> int:
  '''
  j=list(values)[0]
  for i in list(values):
    if abs(one - i) < abs(one - j):
      j = i
    elif abs(one - i) == abs(one - j):
      if j > i:
        j = i
  return j
  '''
  '''
  if one in values:
    return one
  return min(values, key=lambda v: (abs(v - one), v))
  '''
  #return min(sorted(list(values)), key=lambda x: abs(x - one))
  return min((abs(one-i),i) for i in values)[1]

if __name__ == '__main__':
    print("Example:")
    print(nearest_value({0, -2}, -1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    assert nearest_value({0, -2}, -1) == -2
    print("Coding complete? Click 'Check' to earn cool rewards!")