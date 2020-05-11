import numpy as np 


#returns the elements in box i
def box(i, puzzle): 
    ''' For box 1 return first three rows and first three columns,
        For box 2 return first three rows and second three columns,
        For box 3 return first three rows and third three columns,
        For box 4 return second three rows and first three columns,
        For box 5 return second three rows and second three columns,
        For box 6 return second three rows and third three columns,
        For box 7 return third three rows and first three columns,
        For box 8 return third three rows and second three columns,
        For box 9 return third three rows and third three columns
    '''
    col = ((i-1)%3)*3
    if i < 4:
        return puzzle[:3,col:col+3]
    elif i < 7:
        return puzzle[3:6,col:col+3]
    else:
        return puzzle[6:9,col:col+3]


#returns which box the i,j coordinate corresponds to
def which_box(i,j):
    if i < 3:
        if j < 3:
            return 1
        elif j < 6:
            return 2
        else:
            return 3
    elif i < 6:
        if j < 3:
            return 4
        elif j < 6:
            return 5
        else:
            return 6
    else:
        if j < 3:
            return 7
        elif j < 6:
            return 8
        else:
            return 9


#checks to see if element is in the row
def used_in_row(puzzle,row,num):
    for i in range(9):
        if (puzzle[row][i] == num):
            return True
    return False


#checks to see if element is in the column
def used_in_col(puzzle,col,num):
    for i in range(9):
        if (puzzle[i][col] == num):
            return True
    return False


#checks to see if element is in the box
def used_in_box(puzzle,row,col,num):
    if num in box(which_box(row,col),puzzle):
        return True
    return False


#checks to see if element is in the row, column, or box
def used(puzzle,row,col,num):
    return used_in_row(puzzle,row,num) or used_in_col(puzzle,col,num) or used_in_box(puzzle,row,col,num)


#checks if there is an empty cell in the puzzle and updates the 
#coordinates of the first empty cell
def find_empty(puzzle, l):
    for row in range(9):
        for col in range(9):
            if (puzzle[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


#solve puzzle through backtracking algorithm
def backtracking(puzzle):
    #initialize coordinates of empty cell
    l = [0,0]
    #finds first empty cell
    if not find_empty(puzzle,l):
        return True #done (recursion stopping point)
    row = l[0] #row index of empty cell
    col = l[1] #column index of empty cell
    for i in range(1,10):
        #looks to see if element is valid in the empty cell location
        if not used(puzzle,row,col,i): 
            puzzle[row][col] = i
            if backtracking(puzzle):
                return True #no more empty cells (done)
            puzzle[row][col] = 0 
    return False #condition to initialize backtracking


import numpy as np


#test cases
def test_case(i):
    problems = {0: np.array([[0,6,0,0,8,0,4,2,0],
                        [0,1,5,0,6,0,3,7,8],
                        [0,0,0,4,0,0,0,6,0],
                        [1,0,0,6,0,4,8,3,0],
                        [3,0,6,0,1,0,7,0,5],
                        [0,8,0,3,5,0,0,0,0],
                        [8,3,0,9,4,0,0,0,0],
                        [0,7,2,1,3,0,9,0,0],
                        [0,0,9,0,2,0,6,1,0]]),
                1: np.array([[0,0,0,0,3,0,0,0,7],
                        [0,7,0,0,0,0,1,2,0],
                        [1,0,0,0,6,4,5,8,0],
                        [0,0,0,0,0,1,0,0,0],
                        [5,0,0,0,0,9,7,6,0],
                        [7,4,0,0,0,0,0,1,9],
                        [0,0,8,4,2,0,0,0,1],
                        [4,0,2,0,1,0,6,7,8],
                        [0,0,0,0,0,0,0,4,0]]),
                2: np.array([[0,0,0,0,4,9,0,5,0],
                        [7,0,0,5,0,0,9,0,4],
                        [0,0,0,0,0,0,6,1,3],
                        [1,4,0,0,0,0,3,0,8],
                        [0,0,8,0,0,0,5,6,0],
                        [0,0,0,0,0,5,0,0,9],
                        [5,0,0,4,0,0,8,0,0],
                        [9,3,0,0,1,0,0,0,0],
                        [8,0,0,7,0,0,1,0,0]]),
                3: np.array([[0,4,7,0,0,0,9,0,1],
                        [0,0,0,0,0,0,0,0,8],
                        [0,6,0,0,0,0,0,0,5],
                        [0,5,0,7,3,4,0,2,0],
                        [0,0,0,6,8,0,4,0,0],
                        [0,0,0,2,0,0,0,0,0],
                        [4,3,0,0,0,1,0,6,0],
                        [0,0,0,0,7,0,0,0,9],
                        [0,0,1,0,0,0,0,0,0]]) 
                }             

    return problems[i]


if __name__ == '__main__':
    problem = test_case(3)
    solution = np.copy(problem) #make a copy of the problem puzzle to work on
    if backtracking(solution):
        print(solution)