class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = nums[0]
        max_ending_here = nums[0]
        min_ending_here = nums[0]

        for n in nums[1:]:
            candidates = (n, n * max_ending_here, n * min_ending_here)
            max_ending_here = max(candidates)
            min_ending_here = min(candidates)
            largest = max(largest, max_ending_here)

        return largest
