class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        start, end = 0, 0
        counts = {}
        counts[s[0]] = 1
        while True:
            total = end - start + 1
            first = max(counts.values())
            if total - first <= k:
                if total > longest:
                    longest = total
                # expand window
                end += 1
                if end >= len(s):
                    break
                elif s[end] not in counts.keys():
                    counts[s[end]] = 1
                else:
                    counts[s[end]] += 1
            else:
                # shrink window
                counts[s[start]] -= 1
                start += 1
        return longest
