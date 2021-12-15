class Solution:
    def solve(self, nums):
        nums = sorted(nums)
        maxDifference = nums[1] - nums[0]
        for i in range(1, len(nums) - 1):
            difference = nums[i + 1] - nums[i]
            if maxDifference < difference:
                maxDifference = difference
        return maxDifference