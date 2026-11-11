class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n + 1)
        ways[0] = 1
        for w in range(n):
            if w + 1 <= n:
                ways[w + 1] += ways[w]
            if w + 2 <= n:
                ways[w + 2] += ways[w]
        return ways[n]
