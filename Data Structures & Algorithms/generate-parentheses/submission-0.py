class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = [""]
        for i in range(2*n):
            current_parentheses = []
            for p in parentheses:
                lc = self.countChar("(", p)
                rc = self.countChar(")", p)
                if lc < n:
                    current_parentheses.append(p + "(")
                if lc > rc:
                    current_parentheses.append(p + ")")
            parentheses = current_parentheses
        return parentheses

    def countChar(self, c: str, s: str) -> int:
        return len([i for i in s if i == c])
