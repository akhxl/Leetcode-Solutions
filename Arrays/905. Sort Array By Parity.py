#Author: Akhil Sharma
#Date: 10/25/2022

#Algorithm: We use the two pointer method, beg = group of formed even elements in beginning
#end = formed odd group of elements in the end, iterate through using two pointer comparison
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        beg, end = 0, len(nums) -1

        while beg < end:
            if nums[beg] % 2 == 0:
                beg += 1
            else:
                nums[beg], nums[end] = nums[end], nums[beg]
                end -= 1
        return nums
