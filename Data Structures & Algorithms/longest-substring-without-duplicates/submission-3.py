class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        chars = set()
        i, j = 0, 0
        while j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
            else:
                while s[i] != s[j]:
                    chars.remove(s[i])
                    i += 1
                chars.remove(s[i])
                i += 1
            l = len(chars)
            if l > longest:
                longest = l
        return longest
