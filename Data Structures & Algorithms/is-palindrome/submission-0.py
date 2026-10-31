class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = [s[i].lower() for i in range(len(s)) if s[i].isalnum()]
        for i in range(len(alpha)):
            if alpha[i] != alpha[len(alpha) - 1 - i]:
                return False
        return True
