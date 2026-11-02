class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        i = (l + r) // 2
        while l != r:
            if nums[i] == target:
                return i
            if nums[i] > target:
                r = i
            else: # nums[i] < target
                l = i + 1
            i = (l + r) // 2
        return -1
