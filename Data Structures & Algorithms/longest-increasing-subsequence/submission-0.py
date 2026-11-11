class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_ending_at = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_ending_at[i] = max(longest_ending_at[i], longest_ending_at[j] + 1)

        return max(longest_ending_at)
