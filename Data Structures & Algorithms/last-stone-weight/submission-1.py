class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            x = stones.pop()
            y = stones.pop()
            if x == y:
                continue
            else:
                stones.append(x - y)
        return stones[0] if stones else 0
