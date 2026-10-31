class Solution:
    size = 9
    mod = 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        structures = []
        structures.extend(self.rows(board))
        structures.extend(self.cols(board))
        structures.extend(self.grids(board))
        
        for s in structures:
            if self.isDuplicate(s) or self.isOutRange(s):
                return False
        return True

    def rows(self, board):
        rows = [[None] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                rows[i][j] = board[i][j]
        return rows

    def cols(self, board):
        cols = [[None] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                cols[j][i] = board[i][j]
        return cols

    def grids(self, board):
        grids = [[None] * self.size for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                row_q = i // self.mod
                row_r = i % self.mod
                col_q = j // self.mod
                col_r = j % self.mod
                grids[row_q * 3 + col_q][row_r * 3 + col_r] = board[i][j]
        return grids

    def isDuplicate(self, digits):
        for i in range(0, len(digits)):
            if digits[i] == ".":
                continue
            for j in range(i + 1, len(digits)):
                if digits[i] == digits[j]:
                    return True
        return False

    def isOutRange(self, digits):
        for d in digits:
            if d == ".":
                continue
            n = int(d)
            if n < 1 or 9 < n:
                return True
        return False
