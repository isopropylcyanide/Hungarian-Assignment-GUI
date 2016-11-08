
"""Solve Assignment Problem
Subject: Operations Research
Author: Aman Garg
Date: 07/11/2016
"""
from itertools import combinations
from collections import deque
from sys import maxint, argv, exit

n = 0
# denote rows and columns resp. Must be equal for the given matrix


class HorzLine:
    """Denotes a horizontal line across the matrix"""

    def __init__(self, pos):
        self.pos = pos
        self.type = "Horizontal"
        self.across = "row"

    def __repr__(self):
        return 'H%d' % (self.pos)


class VertLine:
    """Denotes a vertical line across the matrix"""

    def __init__(self, pos):
        self.pos = pos
        self.type = "Vertical"
        self.across = "column"

    def __repr__(self):
        return 'V%d' % (self.pos)


def getDummy(M, n, m):
    """Add a dummy variable when rows != columns"""
    _m = max(n, m)
    for i in xrange(_m):
        for j in xrange(_m):
            M[i][j] = 0 if M[i][j] == -1 else M[i][j]
    return M


def readInput():
    """Read matrix from file"""
    global n

    if len(argv) != 2:
        print '\n No input file feeded'
        print ' Usage: python assignment.py "name_of_InputFile"'
        return None

    try:
        inputFile = argv[1]
        f = file(inputFile, "r")
        n, m = map(int, f.readline().strip().split(" "))
        _m = max(n, m)
        M = [[-1 for a in xrange(_m)]
             for b in xrange(_m)]  # denotes the matrix
        for ind, i in enumerate(f.readlines()):
            for indj, j in enumerate(map(int, i.strip().split(" "))):
                M[ind][indj] = j

        if n != m:
            print '\n Matrices aren\'t of the same order'
            print ' Adding dummy\n'
            M = getDummy(M, n, m)
        else:
            print '\n No dummy required'
        n = _m
        return M

    except Exception:
        print '\n File %s not found. Check again' % (inputFile)
        return None


def reduceMat(M):
    """Returns a row and column reduced matrix"""
    for i in xrange(n):
        minElem = min(M[i])
        M[i] = map(lambda x: x - minElem, M[i])

    # Now for column reduction
    for col in xrange(n):
        l = []
        for row in xrange(n):
            l.append(M[row][col])
        minElem = min(l)
        for row in xrange(n):
            M[row][col] -= minElem
    return M


def getZeroPositions(M):
    """Returns current positions of 0's"""
    Z = set()
    for i in xrange(n):
        for j in xrange(n):
            if M[i][j] == 0:
                Z.add((i, j))
    return Z


def getSetOfCrossingLines(M, Z):
    """Returns a set of lines that minimally cover all zeros"""

    horzLines = [HorzLine(i) for i in xrange(n)]
    vertLines = [VertLine(i) for i in xrange(n)]
    # We have to choose maximum n lines for crossing out all zeros
    # The assignment is optimal when the minimal lines are the order of the
    # matrix
    allComb = []
    for i in xrange(1, n + 1):
        allComb.extend(combinations(horzLines + vertLines, i))

    # Find the combination which covers the lists in the minimumLines
    bestComb = []

    for i in allComb:
        covered = set()
        for j in i:
            for zero in Z:
                if zero in covered:
                    continue
                elif j.type == 'Horizontal' and j.pos == zero[0]:
                    covered.add(zero)
                elif j.type == 'Vertical' and j.pos == zero[1]:
                    covered.add(zero)
        if len(covered) == len(Z):
            if bestComb == []:
                bestComb = i
            elif len(i) < len(bestComb):
                bestComb = i

    return bestComb


def checkAssignments(M, Z):
    """What is the minimum assignment possible to cover all zeros"""

    bestComb = getSetOfCrossingLines(M, Z)
    print '\n Current best combination to cover all zeros: ', len(bestComb)
    for i in bestComb:
        print '\t%s line through %s : %d' % (i.type, i.across, i.pos)

    curAssignments, totalVal = getAssignment(Z), 0
    print '\n  The assignments are as follows: \n',
    for i in curAssignments:
        x, y = i[0], i[1]
        print '\t At: ', x, y, ' Value: ',  _backup[x][y]
        totalVal += _backup[x][y]

    if len(bestComb) != n:
        # Perform the following steps
        print '\n Current solution isn\'t optimal as lines are not enough\n'
        tickRowsAndColumns(curAssignments, M, Z)

    else:
        print '\n Current solution is optimal and the minimal cost: ', totalVal
        return


def getAssignment(Z):
    """Asssign maximum number of zeroes possible """
    removedSet = set()

    # As there can be max n zeros
    bestAssign = set()

    # Since there are atleast 4 zeroes in our zeroes, array
    for comb in combinations(Z, n):
        removedSet = set()
        totalSet = set(comb)
        curAssign = set()
        for j in totalSet:
            if j in removedSet:
                continue
            r, c = j[0], j[1]
            # remove others has same row/col
            curAssign.add(j)
            for k in totalSet:
                if k != j and k not in removedSet:
                    if k[0] == r or k[1] == c:
                        removedSet.add(k)
        if len(curAssign) > len(bestAssign):
            bestAssign = curAssign.copy()
    return bestAssign


def tickRowsAndColumns(assignments, M, Z):
    """Tick rows and columns in the Matrix accordingly:
    - Tick rows that do not have an assignment
    - Tick cols that have 0's in the marked row
        - Tick all rows that have assignments in the marked column
        - Repeat the above procedure till no more can be ticked
        QuickThink: Use BFS and sets for row/cols
    """
    tickRows, tickCols = set(xrange(n)), set()
    # Tick rows without assignment
    for i in assignments:
        curRow = i[0]
        if curRow in tickRows:
            tickRows.remove(curRow)

    queue = deque(tickRows)
    while queue:
        # Tick cols that have 0's in ticked row
        queue.popleft()
        for row in tickRows:
            for col in xrange(n):
                if M[row][col] == 0:
                    tickCols.add(col)

        for col in tickCols:
            for assign in assignments:
                if assign[1] == col and assign[0] not in tickRows:
                    tickRows.add(assign[0])
                    queue.append(assign[0])

    print '\n Ticked rows:  ', list(tickRows)
    print ' Ticked cols:  ', list(tickCols)

    # Draw straight lines through unmarked rows and marked columns
    horLines = [HorzLine(i) for i in xrange(n) if i not in tickRows]
    verLines = [VertLine(i) for i in xrange(n) if i in tickCols]
    bestComb = horLines + verLines

    print '\n Marking unmarked rows and marked cols:  ', len(bestComb)
    for i in bestComb:
        print '\t%s line through %s : %d' % (i.type, i.across, i.pos)

    if horLines + verLines == n:
        print '\n Current solution is optimal'
        curAssignments, totalVal = getAssignment(Z), 0
        print '\n  The assignments are as follows: \n',
        for i in curAssignments:
            x, y = i[0], i[1]
            print '\t At: ', x, y, ' Value: ',  _backup[x][y]
            totalVal += _backup[x][y]
        return True
    else:
        print '\n Current solution isn\'t optimal as lines are not enough'
        print ' Now going for uncovering elements pass'
        M = smallestElements(bestComb, M)
        Z = getZeroPositions(M)
        print '\n New Zeros are located at follows:',
        for i in Z:
            print i,
        print
        checkAssignments(M, Z)


def smallestElements(bestComb, M):
    """
    Examine uncovered elements: Select min uncovered and subtract from all
    uncovered elements. For elements at intersection of two lines, add the min
    element, for rest : as it is
    """
    H_MASK, V_MASK, I_MASK = "H", "V", "I"
    MASK = [[None for i in xrange(n)] for j in xrange(n)]

    for line in bestComb:
        if line.type == "Horizontal":
            row = line.pos
            for col in xrange(n):
                if MASK[row][col] is None:
                    MASK[row][col] = H_MASK
                elif MASK[row][col] == V_MASK:
                    MASK[row][col] = I_MASK

        elif line.type == "Vertical":
            col = line.pos
            for row in xrange(n):
                if MASK[row][col] is None:
                    MASK[row][col] = V_MASK
                elif MASK[row][col] == H_MASK:
                    MASK[row][col] = I_MASK

    minElem = maxint
    for i in xrange(n):
        for j in xrange(n):
            if MASK[i][j] == None:
                minElem = min(minElem, M[i][j])
    # Subtract min from uncovered, and add to intersection elems
    for i in xrange(n):
        for j in xrange(n):
            if MASK[i][j] == None:
                M[i][j] -= minElem
            elif MASK[i][j] == I_MASK:
                M[i][j] += minElem

    print '\n Uncovered matrix',
    printMatrix(M)
    return M


def printMatrix(M):
    print
    for i in M:
        for j in i:
            print ' ', j, ' ',
        print
    print


if __name__ == '__main__':
    # Obtain matrix from file
    M = readInput()
    if M is None:
        print ' Error occured during execution\n'
        exit()
    _backup = M[:]
    print '\n Matrix as in file:',
    printMatrix(M)

    # Reduce the matrix
    M = reduceMat(M)
    print '\n Reduced Matrix:',
    printMatrix(M)

    # Get zero positions from the array
    Z = getZeroPositions(M)
    print '\n Zeros are located at follows:',
    for i in Z:
        print i,
    print

    # Check assignments
    checkAssignments(M, Z)
