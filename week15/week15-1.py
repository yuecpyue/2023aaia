class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()#排好
        return nums[-1]*nums[-2]-nums[1]*nums[0]