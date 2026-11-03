class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        i, j = 0, l - 1
        while i != j:
            k = (i + j) // 2
            if nums[k] > nums[j]:
                i = k + 1
            else: # nums[k] < nums[j]:
                j = k
        return nums[i]
