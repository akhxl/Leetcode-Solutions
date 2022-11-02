#Author: Akhil Sharma
#Date: 10/25/2022

#Algorithm: Set will automatically remove duplicates so check if set size is = list size
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if numset.length != nums.length:
            return false
