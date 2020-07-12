#!/usr/bin/env python
# -*- coding:utf-8 -*-
def find_message(text: str) -> str:
    """Find a secret message"""
    result=""
    for ch in text:
        if(ch.isupper()):
            result += ch
    return result

if __name__ == '__main__':
    print('Example:')
    print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
