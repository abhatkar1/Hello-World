# (Game: Eight Queens) The classic Eight Queens puzzle is to place eight
# queens on a chessboard such that no two queens can attack each other (i.e., no
# two queens are in the same row, same column, or same diagonal). There are
# many possible solutions.

def search(row):
    if row == SIZE:
        return True

    for column in range(SIZE):
        queen[row] = column
        if isValid(row, column) and search(row + 1):
            return True

    return False

def isValid(row, column):
    for i in range(1, row + 1):
        if (queen[row - i] == column \
            or queen[row - i] == column + i \
            or queen[row - i] == column - i):
            return False
    return True

SIZE = 8

queen = SIZE * [-1]

search(0)

chessboard = [(SIZE * [x]) for x in SIZE * [0]]

def setQueens():
    for i in range(len(queen)):
        chessboard[i][queen[i]] = 'Q'


def printMatrix2D():
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            print(chessboard[i][j], end = " ")
        print()

setQueens()

printMatrix2D()



# print(queen)