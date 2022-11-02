#Author: Akhil Sharma
#Date: 11/01/2022

#Algorithm: chain groups all iterables and produces a single iterable as output, 
#thus we chain the tuples formed from zipping the list to everything after n

from itertools import chain
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return chain(*zip(nums, nums[n:]))