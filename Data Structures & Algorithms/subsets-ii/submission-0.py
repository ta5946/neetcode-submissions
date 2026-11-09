class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sorted_nums = sorted(nums)
        subsets = []
        subsets.append([])
        num_counts = Counter(nums)
        for n, c in num_counts.items():
            num_subsets = subsets.copy()
            for s in subsets:
                for i in range(1, c + 1):
                    subset = s.copy()
                    for j in range(i):
                        subset.append(n)
                    num_subsets.append(subset)
            subsets = num_subsets.copy()
        return subsets
