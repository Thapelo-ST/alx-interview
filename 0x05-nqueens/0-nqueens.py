#!/usr/bin/env python3
import sys

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def is_safe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_nqueens_util(self, col):
        if col == self.n:
            self.print_solution()
            return True

        res = False
        for i in range(self.n):
            if self.is_safe(i, col):
                self.board[i][col] = 1

                res = self.solve_nqueens_util(col + 1) or res

                self.board[i][col] = 0

        return res

    def solve_nqueens(self):
        if not isinstance(self.n, int):
            print("N must be a number")
            sys.exit(1)

        if self.n < 4:
            print("N must be at least 4")
            sys.exit(1)

        if not self.solve_nqueens_util(0):
            print(f"No solution for N = {self.n}")

    def print_solution(self):
        solution = []
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    solution.append([i, j])
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solver = NQueensSolver(N)
        solver.solve_nqueens()
    except ValueError:
        print("N must be a number")
        sys.exit(1)
