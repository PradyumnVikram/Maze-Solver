class Solver:
    def __init__(self, n_size, board):
        self.n_size = n_size
        self.board = board

    def print_board(self, board):
        for i in board:
            print()
            for j in i:
                print(j, end=' ')

    def solve_maze(self):
        count = 0
        if not self.solve(self.board, 0, 0):
            return False
        return self.board

    def isValid(self, x, y):
        if x >= 0 and x < self.n_size and y >= 0 and y < self.n_size and self.board[x][y] == 1:
            return True
        return False

    def solve(self, board, x, y):
        if x == self.n_size - 1 and y == self.n_size - 1 and self.board[x][y] == 1:
            self.board[x][y] = 2
            return True

        if self.isValid(x, y):
            self.board[x][y] = 2

            if self.solve(self.board, x, y + 1):
                return True

            if self.solve(self.board, x + 1, y):
                return True

            self.board[x][y] = 0
            return False


def new_board(n_size):
    return [[1 for n in range(n_size)] for row in range(n_size)]
