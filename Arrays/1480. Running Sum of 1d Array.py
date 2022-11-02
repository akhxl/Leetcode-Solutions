#Author: Akhil Sharma
#Date: 11/01/2022

#Algorithm: either use itertools accumulate or just prefix sum or prefix sum

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        return [s := s + num for _, num in enumerate(nums)]