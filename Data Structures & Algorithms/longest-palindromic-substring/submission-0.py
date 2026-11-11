class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > len(longest):
                    longest = s[l + 1: r]
        return longest
