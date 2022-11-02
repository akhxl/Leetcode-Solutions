#Author: Akhil Sharma
#Date: 11/01/2022

#Algorithm: We use the collections.Counter(nums).values() to access the duplicate counts,
#for any n duplicate count there are n-1 good pairs stemming from that and then n-2, so take sum
import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(k * (k - 1) / 2 for k in collections.Counter(nums).values())