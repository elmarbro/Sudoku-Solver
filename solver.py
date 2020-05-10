import numpy as np 

# problem = np.array([[0,6,0,0,8,0,4,2,0],
#                     [0,1,5,0,6,0,3,7,8],
#                     [0,0,0,4,0,0,0,6,0],
#                     [1,0,0,6,0,4,8,3,0],
#                     [3,0,6,0,1,0,7,0,5],
#                     [0,8,0,3,5,0,0,0,0],
#                     [8,3,0,9,4,0,0,0,0],
#                     [0,7,2,1,3,0,9,0,0],
#                     [0,0,9,0,2,0,6,1,0]])


# problem = np.array([[0,0,0,0,3,0,0,0,7],
#                     [0,7,0,0,0,0,1,2,0],
#                     [1,0,0,0,6,4,5,8,0],
#                     [0,0,0,0,0,1,0,0,0],
#                     [5,0,0,0,0,9,7,6,0],
#                     [7,4,0,0,0,0,0,1,9],
#                     [0,0,8,4,2,0,0,0,1],
#                     [4,0,2,0,1,0,6,7,8],
#                     [0,0,0,0,0,0,0,4,0]])


# problem = np.array([[0,0,0,0,4,9,0,5,0],
#                     [7,0,0,5,0,0,9,0,4],
#                     [0,0,0,0,0,0,6,1,3],
#                     [1,4,0,0,0,0,3,0,8],
#                     [0,0,8,0,0,0,5,6,0],
#                     [0,0,0,0,0,5,0,0,9],
#                     [5,0,0,4,0,0,8,0,0],
#                     [9,3,0,0,1,0,0,0,0],
#                     [8,0,0,7,0,0,1,0,0]])


problem = np.array([[0,4,7,0,0,0,9,0,1],
                    [0,0,0,0,0,0,0,0,8],
                    [0,6,0,0,0,0,0,0,5],
                    [0,5,0,7,3,4,0,2,0],
                    [0,0,0,6,8,0,4,0,0],
                    [0,0,0,2,0,0,0,0,0],
                    [4,3,0,0,0,1,0,6,0],
                    [0,0,0,0,7,0,0,0,9],
                    [0,0,1,0,0,0,0,0,0]])                    


solution = np.copy(problem)


def valid_row(row):
    for i in range(9):
        if np.count_nonzero(row == i+1) > 1:
            return False
    return True


def valid_column(column):
    for i in range(9):
        if np.count_nonzero(column == i+1) > 1:
            return False
    return True


def valid_box(box):
    for i in range(9):
        if np.count_nonzero(box == i+1) > 1:
            return False
    return True


def row(i, puzzle): #return row i
    return puzzle[i]


def column(j, puzzle): #return column i
    return puzzle[:,j]


def box(i, puzzle): #return box i 
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


def valid(puzzle): #currently not used
    for i in range(9):
        if not valid_row(row(i, puzzle)) or not valid_column(column(i, puzzle)) or not valid_box(box(i, puzzle)):
            return False
    return True


def valid_element(i,j,puzzle):
    if not valid_row(row(i,puzzle)) or not valid_column(column(i,puzzle)) or not valid_box(box(which_box(i,j),puzzle)):
        return False
    return True


def valid_solution(): #currently not used
    if (not np.count_nonzero(solution == 0)) and valid():
        return True
    return False


def valid_elements(i,j):
    if solution[i][j] != 0:
        return [solution[i][j]]
    possible = []
    test = np.copy(solution)
    for n in range(9):
        test[i][j] = n+1
        row_test = row(i, test)
        column_test = column(j, test)
        box_test = box(which_box(i,j), test)
        if valid_row(row_test) and valid_column(column_test) and valid_box(box_test):
            possible.append(n+1)
    return possible


def possible_elements():
    elements = {}
    for i in range(9):
        for j in range(9):
            elements["{}_{}".format(i,j)] = valid_elements(i,j)
    return elements


def solve():
    current = np.count_nonzero(solution == 0)
    previous = current+1
    while current < previous:
        previous = current
        elements = possible_elements()
        for i in range(9):
            for j in range(9):
                values = elements["{}_{}".format(i,j)]
                if len(values) == 1:
                    solution[i][j] = values[0]
        current = np.count_nonzero(solution == 0)
    return solution


def used_in_row(puzzle,row,num):
    for i in range(9):
        if (puzzle[row][i] == num):
            return True
    return False


def used_in_col(puzzle,col,num):
    for i in range(9):
        if (puzzle[i][col] == num):
            return True
    return False


def used_in_box(puzzle,row,col,num):
    if num in box(which_box(row,col),puzzle):
        return True
    return False


def used(puzzle,row,col,num):
    return used_in_row(puzzle,row,num) or used_in_col(puzzle,col,num) or used_in_box(puzzle,row,col,num)


def find_empty(puzzle, l):
    for row in range(9):
        for col in range(9):
            if (puzzle[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def backtracking(puzzle):
    l = [0,0]
    if not find_empty(puzzle,l):
        return True
    row = l[0]
    col = l[1]
    for i in range(1,10):
        if not used(puzzle,row,col,i):
            puzzle[row][col] = i
            if backtracking(puzzle):
                return True
            puzzle[row][col] = 0
    return False

if __name__ == '__main__':
    if backtracking(solution):
        print(solution)