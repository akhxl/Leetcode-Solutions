#Author: Akhil Sharma
#Date: 11/02/2022

#Algorithm: use strip() to remove spaces, split() to separate words, take max len using list comp

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(txt.strip().split()) for txt in sentences)