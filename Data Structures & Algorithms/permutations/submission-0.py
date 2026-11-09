class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.generate(nums, 0, permutations)
        return permutations

    def generate(self, nums: List[int], start: int, permutations: List[List[int]]) -> None:
        if start == len(nums):
            permutations.append(nums)
            return

        for i in range(start, len(nums)):
            new_nums = nums.copy()
            new_nums[start], new_nums[i] = new_nums[i], new_nums[start]
            self.generate(new_nums, start + 1, permutations)
