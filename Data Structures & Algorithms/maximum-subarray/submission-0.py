class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        sum_ending_here = 0

        for num in nums:
            sum_ending_here = max(num, sum_ending_here + num)
            maximum = max(maximum, sum_ending_here)

        return maximum
