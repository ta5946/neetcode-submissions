class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        i = 0
        j = l - 1
        while i < j:
            current = numbers[i] + numbers[j]
            if current == target:
                return [i + 1, j + 1]
            elif current < target:
                i += 1
            elif current > target:
                j -= 1
