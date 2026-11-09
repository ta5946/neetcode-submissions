class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        num_counts = Counter(nums)
        for n, c in num_counts.items():
            current_subsets = subsets.copy()
            for s in subsets:
                for i in range(1, c + 1):
                    subset = s.copy()
                    for j in range(i):
                        subset.append(n)
                    current_subsets.append(subset)
            subsets = current_subsets
        return subsets
