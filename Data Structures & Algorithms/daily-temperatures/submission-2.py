class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        end = 0
        while True:
            # fill stack
            while end < len(temperatures) and (len(stack) == 0 or temperatures[end] <= temperatures[stack[-1]]):
                stack.append(end)
                end += 1
            if end == len(temperatures):
                break
            # empty stack
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[end]:
                start = stack.pop()
                result[start] = end - start
        return result
