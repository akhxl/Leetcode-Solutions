#Author: Akhil Sharma
#Date: 10/25/2022

#Algorithm: defaultdict, key value hashmap

from collections import defaultdict

class Solution:
    def groupAnagram(self, strs: List[str]) -> List[List[str]]:
        letter_word = defaultdict(list)
        for word in str:
            letter_word[tuple(word)].append(word)
        return list(letter_word.values())