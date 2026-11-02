class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for t in tokens:
            if t in operators:
                n2 = stack.pop()
                n1 = stack.pop()
                if t == "+":
                    res = n1 + n2
                elif t == "-":
                    res = n1 - n2
                elif t == "*":
                    res = int(n1 * n2)
                else: # t == "/":
                    res = int(n1 / n2)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack.pop()            
