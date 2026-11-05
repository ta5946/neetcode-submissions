class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counts = {}
        for c in candidates:
            counts[c] = counts.get(c, 0) + 1
        self.counts = sorted(counts.items())

        self.combinations = []
        self.buildCombinations([], 0, target)
        return self.combinations

    def buildCombinations(self, current, index, target):
        if target == 0:
            self.combinations.append(current)
            return
        if target < 0 or index >= len(self.counts):
            return

        value, count = self.counts[index]
        for k in range(count + 1):
            if k * value > target:
                break
            self.buildCombinations(current + [value] * k, index + 1, target - k * value)
