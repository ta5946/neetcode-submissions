class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for n in nums:
            if n not in c:
                c[n] = 1
            else:
                c[n] += 1
        sorted_nums = sorted(c.keys(), key=lambda n: c[n], reverse=True)
        return sorted_nums[:k]
