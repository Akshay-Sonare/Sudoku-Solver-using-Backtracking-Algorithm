'''
Project Name: Sudoku Solver
Purpose: To solve incomplete sudoku using backtracking algorithm.
Input : 9*9 Matrix
output: 9*9 solved Matrix
'''
SIZE = 9 #Size of the matrix

matrix = [
    [6,5,0,8,7,3,0,9,0],
    [0,0,3,2,5,0,0,0,8],
    [9,8,0,1,0,4,3,5,7],
    [1,0,5,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,2],
    [0,0,0,0,0,0,5,0,3],
    [5,7,8,3,0,1,0,2,6],
    [2,0,0,0,4,8,9,0,0],
    [0,9,0,6,2,5,0,8,1]]

def sudoku_print():
    for i in matrix:
        print(i)

#identify unassigned numbers in a matrix

def number_unassigned(row, col):
    unassigned_number = 0
    for i in range(0,SIZE):
        for j in range(0,SIZE):
            if (matrix[i][j] == 0):
                row = i
                col = j
                unassigned_number = 1
                a= [row, col, number_unassigned]
                return a
    a = [-1, -1, unassigned_number]
    return a

def is_safe(num, row, col):
    #check if number present in row
    for i in range(0, SIZE):
        if(matrix[row][i] == num):
            return False
    
    #check if number present in col
    for j in range(0, SIZE):
        if(matrix[j][col] == num):
            return False

    #check if number is present in diagonal 
    row_start = (row//3)*3
    col_start = (col//3)*3
    for k in range(row_start, row_start+3):
        for l in range(col_start, col_start+3):
            if (matrix[k][l] == num):
                return False

    return True

def sudoku_solver():
    row = 0
    col = 0
    a = number_unassigned(row,col)
    if(a[2] == 0):
        return True
    row = a[0]
    col = a[1]

    for i in range(1, SIZE+1):
        if(is_safe(i, row, col)):
            matrix[row][col] = i
            #Backtracking
            if(sudoku_solver()):
                return True

            matrix[row][col] = 0
    return False

if sudoku_solver():
    print('Solved Sudoku:')
    sudoku_print()
else:
    print('No Solution')
               


