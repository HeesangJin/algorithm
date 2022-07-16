# https://leetcode.com/problems/valid-palindrome/
import collections
from typing import Deque


def __main__():
    s = "A man, a plan, a canal: Panama"
    strs: Deque = collections.deque()
    for char in s:
        if char.isalnum():  # if alphabet or num
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True
