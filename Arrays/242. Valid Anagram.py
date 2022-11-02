#Author: Akhil Sharma
#Date: 10/25/2022

#Algorithm: Anagram means same letters are used so just check if each sorted is equivalent
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (sorted(s) == sorted(t)):
            return True