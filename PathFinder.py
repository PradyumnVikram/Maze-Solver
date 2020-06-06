class Solver:
    def __init__(self, n_size, board):
        self.n_size = n_size
        self.board = board

    def print_board(self, board):
        for i in board:
            print()
            for j in i:
                print(j, end=' ')

    def solve_maze(self, final, start):
        count = 0
        if not self.solve(self.board, start[0],start[1], final):
            return False
        return self.board

    def isValid(self, x, y):
        if x >= 0 and x < self.n_size and y >= 0 and y < self.n_size and self.board[x][y] == 1:
            return True
        return False

    def solve(self, board, x, y, final):
        if x == final[0] and y == final[1] and self.board[x][y] == 4:
            self.board[x][y] = 2
            return True

        if self.isValid(x, y):
            self.board[x][y] = 2

            if self.solve(self.board, x, y + 1, final):
                return True

            if self.solve(self.board, x + 1, y, final):
                return True
            if self.solve(self.board, x - 1, y, final):
                return True
            if self.solve(self.board, x, y - 1, final):
                return True

            self.board[x][y] = 5
            return False


def new_board(n_size):
    return [[1 for n in range(n_size)] for row in range(n_size)]
