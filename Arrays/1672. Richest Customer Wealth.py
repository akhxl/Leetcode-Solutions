#Author: Akhil Sharma
#Date: 11/01/2022

#Algorithm: take the max of the map of the sum function to the accounts and return it 
#map function takes the sum of each entry of accounts and takes the max between

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))