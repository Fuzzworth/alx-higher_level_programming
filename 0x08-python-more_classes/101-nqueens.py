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
    matrix = [[0] * size for _ in range(size)]
    return matrix


ld = [0] * (N*N)
rd = [0] * (N*N)
cl = [0] * (N*N)
 
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
 
def solveNQUtil(board, col):
 
    # Base case: If all queens are placed
    # then return True
    if (col >= N):
        return True
 
    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
 
        # Check if the queen can be placed on board[i][col]
 
        # To check if a queen can be placed on
        # board[row][col] We just need to check
        # ld[row-col+n-1] and rd[row+coln]
        # where ld and rd are for left and
        # right diagonal respectively
        if ((ld[i - col + N - 1] != 1 and
             rd[i + col] != 1) and cl[i] != 1):
 
            # Place this queen in board[i][col]
            board[i][col] = 1
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 1
 
            # Recur to place rest of the queens
            if (solveNQUtil(board, col + 1)):
                return True
 
            # If placing queen in board[i][col]
            # doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0  # BACKTRACK
            ld[i - col + N - 1] = rd[i + col] = cl[i] = 0
 
            # If the queen cannot be placed in
            # any row in this column col then return False
    return False
 
 
# This function solves the N Queen problem using
# Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns False if queens
# cannot be placed, otherwise, return True and
# prints placement of queens in the form of 1s.
# Please note that there may be more than one
# solutions, this function prints one of the
# feasible solutions.
def solveNQ():
    board = generate_matrix(N)
    if (solveNQUtil(board, 0) == False):
        printf("Solution does not exist")
        return False
    printSolution(board)
    return True
 
 
# Driver Code
if __name__ == '__main__':
    solveNQ()
