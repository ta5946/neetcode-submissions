class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = 0
        skipped = 0
        for n in nums:
            robbed, skipped = skipped + n, max(robbed, skipped)
        return max(robbed, skipped)
