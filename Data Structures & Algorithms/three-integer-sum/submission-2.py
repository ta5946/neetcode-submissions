class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l = len(nums)
        triplets = []
        for i in range(0, l):
            j = i + 1
            k = l - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    t = sorted([nums[i], nums[j], nums[k]])
                    if t not in triplets:
                        triplets.append(t)
                    j += 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return triplets

        """
        triplets = []
        l = len(nums)
        for i in range(0, l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = sorted([nums[i], nums[j], nums[k]])
                        if t not in triplets:
                            triplets.append(t)
        return triplets
        """
