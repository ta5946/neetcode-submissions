class Solution:
    def numDecodings(self, s: str) -> int:
        valid_codes = {str(i) for i in range(1, 27)}
        n = len(s)

        # decodings[i] = number of ways to decode the first i characters
        decodings = [0] * (n + 1)
        decodings[0] = 1

        for i in range(1, n + 1):
            one_digit = s[i-1]
            if one_digit in valid_codes:
                decodings[i] += decodings[i-1]

            two_digits = s[i-2:i]
            if i >= 2 and two_digits in valid_codes:
                decodings[i] += decodings[i-2]

        return decodings[n]
