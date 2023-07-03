#!/usr/bin/python3
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = sys.argv[1]
    N = int(N)
except TypeError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

def generate_matrix(size):
    """
    Generates a square matrix with 0 values.

    Args:
        size (int): The size of the square matrix.

    Returns:
        list: A square matrix with dimensions `size x size` filled with 0 values.
    """
    matrix = [["." for i in range(size)] for j in range(size)]
    return matrix


def create_list(board, n):
    matrix = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == "Q":
                matrix.append([i, j])
    return matrix


def add_sol(board, ans, n):
    temp = []
    for i in range(n):
        string = ""
        for j in range(n):
            string += board[i][j]
        temp.append(string)
    ans.append(temp)


def is_safe(row, col, board, n):
    x = row
    y = col

    while x >= 0:
        if board[x][y] == "Q":
            return False
        else:
            x -= 1

    x = row
    y = col
    while(y < n and x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            y += 1
            x -= 1

    x = row
    y = col
    while(y >= 0 and x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            x -= 1
            y -= 1
    return True


def solveNQueens(row, ans, board, n):

    if row == n:
        add_sol(board, ans, n)
        return

    for col in range(n):

        if is_safe(row, col, board, n):

            board[row][col] = "Q"
            solveNQueens(row + 1, ans, board, n)

            board[row][col] = "."

if __name__ == "__main__":

    board = generate_matrix(N)

    ans = []
    solveNQueens(0, ans, board, N)

    if len(ans) == 0:
        print()
    else:
        for i in ans:
            print(create_list(i, N))
