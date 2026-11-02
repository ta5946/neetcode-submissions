class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = self.max_pile(piles)

        # binary search
        l = 1
        r = max_pile
        while l < r:
            k = (l + r) // 2
            if self.simulate(piles, k) > h:
                l = k + 1
            else:
                r = k
        return (l + r) // 2

    def max_pile(self, piles):
        max_p = piles[0]
        for p in piles[1:]:
            if p > max_p:
                max_p = p
        return max_p

    def simulate(self, piles, rate):
        hours = 0
        for p in piles:
            hours += p // rate
            if p % rate != 0:
                hours += 1
        return hours
