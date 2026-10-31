class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = [c.lower() for c in s if c.isalnum()]
        return alpha == alpha[::-1]
