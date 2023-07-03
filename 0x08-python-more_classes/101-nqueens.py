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
# Print the board
def print_board(board, n):
    matrix = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == "Q":
                matrix.append([i, j])
    return matrix
 
# Joining '.' and 'Q'
# making combined 2D Array
# For output in desired format
def add_sol(board, ans, n):
    temp = []
    for i in range(n):
        string = ""
        for j in range(n):
            string += board[i][j]
        temp.append(string)
    ans.append(temp)
     
     
# We need to check in three directions
# 1. in the same column above the current position
# 2. in the left top diagonal from the given cell
# 3. in the right top diagonal from the given cell
def  is_safe(row, col, board, n):
    x = row
    y = col
     
    # Check for same upper col
    while(x>=0):
        if board[x][y] == "Q":
            return False
        else:
            x -= 1
             
    # Check for Upper Right Diagonal
    x = row
    y = col
    while(y<n and x>=0):
        if board[x][y] == "Q":
            return False
        else:
            y += 1
            x -= 1
             
    # Check for Upper Left diagonal
    x = row
    y = col
    while(y>=0 and x>=0):
        if board[x][y] == "Q":
            return False
        else:
            x -= 1
            y -= 1
    return True   
 
 
# Function to solve n queens
# solveNQueens function here will fill the queens
# 1. there can be only one queen in one row
# 2. if we filled the final row in the board then row will
# be equal to total number of rows in board
# 3. push that board configuration in answer set because
# there will be more than one answers for filling the board
# with n-queens
def solveNQueens(row, ans, board, n):
     
    # Base Case
    # Queen is depicted by "Q"
    # adding solution to final answer array
    if row == n:
        add_sol(board, ans, n)
        return
     
    # Solve 1 case and rest recursion will follow
    for col in range(n):
         
        # For each position check if it is safe and if it
        # is safe make a recursive call with
        # row+1, board[i][j]='Q' and then revert the change
        # in board that is make the board[i][j]='.' again to
        # generate more solutions
        if is_safe(row, col, board, n):
             
            # If placing Queen is safe
            board[row][col] = "Q"
            solveNQueens(row+1, ans, board, n)
             
            # Backtrack
            board[row][col] = "."
 
 
# Driver Code
if __name__ == "__main__":
     
     
    # 2D array of string will make our board
    # which is initially all empty
    board = generate_matrix(N)
     
    # Store all the possible answers
    ans = []
    solveNQueens(0, ans, board, N)
     
    if ans == []:
        print("Solution does not exist")
    else:
        for i in ans:
            print(print_board(i, N))
         
    # This code is contributed by Priyank Namdeo
