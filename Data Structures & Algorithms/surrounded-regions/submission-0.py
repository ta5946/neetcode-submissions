class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.n = len(board)
        self.m = len(board[0])
        for i in range(self.n):
            for j in range(self.m):
                if i == 0 or j == 0 or i == self.n - 1 or j == self.m - 1:
                    self.markSafe(i, j)
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == "O":
                    self.board[i][j] = "X"
                elif self.board[i][j] == "T":
                    self.board[i][j] = "O"

    def markSafe(self, i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= self.n or j >= self.m or self.board[i][j] != "O":
            return
        self.board[i][j] = "T"
        coordinates = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for c in coordinates:
            self.markSafe(c[0], c[1])
