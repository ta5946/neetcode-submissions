class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in {"(", "{", "["}:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                elif p == ")" and stack.pop() == "(":
                    continue
                elif p == "}" and stack.pop() == "{":
                    continue
                elif p == "]" and stack.pop() == "[":
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
