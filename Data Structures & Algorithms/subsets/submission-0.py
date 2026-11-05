class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for n in nums:
            for s in subs.copy():
                c = s.copy()
                c.append(n)
                subs.append(c)
        return subs
