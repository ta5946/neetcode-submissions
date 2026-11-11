class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        self.dynamic_grid = grid.copy()
        island_count = 0
        for i in range(self.n):
            for j in range(self.m):
                if self.dynamic_grid[i][j] == "1":
                    island_count += 1
                    self.sinkIsland(i, j)
        return island_count
        
    def sinkIsland(self, i, j):
        if i < 0 or j < 0 or i >= self.n or j >= self.m or self.dynamic_grid[i][j] == "0":
            return
        else:
            self.dynamic_grid[i][j] = "0"
            self.sinkIsland(i - 1, j)
            self.sinkIsland(i + 1, j)
            self.sinkIsland(i, j - 1)
            self.sinkIsland(i, j + 1)
