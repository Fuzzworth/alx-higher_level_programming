#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. Write a program that solves the N queens problem.

Notes:
    credit to geeks for geeks for the algo and explanation
    https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    N = sys.argv[1]
    N = int(N)
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)


def generate_matrix(N):
    """
    Generates a square matrix with "." values.

    Args:
        N (int): The size of the square matrix.

    Returns:
        list: A square matrix with dimensions `size x size`
        filled with "." values.
    """
    board = [["." for row in range(N)] for column in range(N)]
    return board


def create_list(board, N):
    """
    Creates a List from the Matrix

    Args:
        board: Matrix
        N: N

    Returns:
        list: list of positions
    """
    matrix = []
    for row in range(N):
        for column in range(N):
            if board[row][column] == "X":
                matrix.append([row, column])
    return matrix


def add_to_results(board, results_list, N):
    """
    Add solution to results

    Args:
        board (list): board
        results_list (list): list of results
        N (int): N
    """
    temp = []
    for row in range(N):
        string = ""
        for column in range(N):
            string += board[row][column]
        temp.append(string)
    results_list.append(temp)


def is_safe(row, column, board, N):
    """
    Checks If addition is safe

    Args:
        row (int): row
        column (int): column
        board (list): board
        N (int): N

    Returns:
        bool: True if safe False if not
    """
    x = row
    y = column

    while x >= 0:
        if board[x][y] == "X":
            return False
        else:
            x -= 1

    x = row
    y = column
    while (y < N and x >= 0):
        if board[x][y] == "X":
            return False
        else:
            y += 1
            x -= 1

    x = row
    y = column
    while (y >= 0 and x >= 0):
        if board[x][y] == "X":
            return False
        else:
            x -= 1
            y -= 1
    return True


def NQueens(row, results_list, board, N):
    """
    Recursive function to solve NQueens

    Args:
        row (int): row
        results_list (list): results_list
        board (list): board
        N (int): N
    """
    if row == N:
        add_to_results(board, results_list, N)
        return

    for column in range(N):
        if is_safe(row, column, board, N):
            board[row][column] = "X"
            NQueens(row + 1, results_list, board, N)
            board[row][column] = "."


if __name__ == "__main__":

    board = generate_matrix(N)

    results_list = []
    NQueens(0, results_list, board, N)

    if len(results_list) != 0:
        for result in results_list:
            print(create_list(result, N))
