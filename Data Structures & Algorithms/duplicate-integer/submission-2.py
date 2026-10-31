class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for n in nums:
            if n in seen.keys():
                return True
            else:
                seen[n] = True
        return False

        """
        l = len(nums)
        for i in range(0, l):
            for j in range(i + 1, l):
                if nums[i] == nums[j]:
                    return True
        return False
        """