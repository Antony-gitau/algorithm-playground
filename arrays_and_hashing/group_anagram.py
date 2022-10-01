#given a list of string as inputs, output group of anagram strings.

from collections import defaultdict
from email.policy import default
from itertools import count
from typing import List


class Solution:
    #function group anagram, get a list of strings as inputs 
    #another list as output
    def groupAnagram(self, strin: List[str])-> List[List[str]]:
        result = defaultdict(list)

        for s in strin:
            count = [0] * 26 

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            result[tuple(count)].append(s)

        return result.values()
        

