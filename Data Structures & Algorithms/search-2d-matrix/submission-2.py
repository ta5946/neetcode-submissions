class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n
        while l != r:
            h = (l + r) // 2
            i = h // n
            j = h % n
            current = matrix[i][j]
            if current == target:
                return True
            elif current < target:
                l = h + 1
            else: # current > target:
                r = h
        return False
