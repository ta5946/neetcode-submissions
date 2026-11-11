class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        current_grid = grid
        minutes = 0
        rotted = 1  # arbitrary

        while not self.allRotten(current_grid) and rotted > 0:
            next_grid = [row.copy() for row in current_grid]
            rotted = 0
            for i in range(n):
                for j in range(m):
                    if current_grid[i][j] == 2:
                        neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                        for x, y in neighbors:
                            if 0 <= x < n and 0 <= y < m and next_grid[x][y] == 1:
                                next_grid[x][y] = 2
                                rotted += 1
            minutes += 1
            current_grid = next_grid

        return minutes if self.allRotten(current_grid) else -1

    def allRotten(self, grid) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return False
        return True
