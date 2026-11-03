class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        i, j = 0, l - 1
        while i <= j:
            k = (i + j) // 2
            if nums[k] == target:
                return k
            if nums[i] <= nums[k]:
                # left half is sorted
                if nums[i] <= target < nums[k]:
                    j = k - 1
                else:
                    i = k + 1
            else:
                # right half is sorted
                if nums[k] < target <= nums[j]:
                    i = k + 1
                else:
                    j = k - 1
        return -1
