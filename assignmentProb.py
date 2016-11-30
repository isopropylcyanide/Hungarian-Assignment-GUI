"""Solve Assignment Problem
Subject: Operations Research
Author: Aman Garg
Date: 07/11/2016
"""
from itertools import combinations
from collections import deque
from sys import maxint, argv, exit


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


class HungarianAssignment:
    """A class that solves the HungarianAssignment problem"""

    def __init__(self):
        self.row, self.col, self.M = 0, 0, None
        self.Z = None

    def printMatrix(self):
        print
        for i in self.M:
            for j in i:
                print ' ', j, ' ',
            print
        print

    def reduceMatrix(self):
        """Returns a row and column reduced matrix"""
        for i in xrange(self.row):
            minElem = min(self.M[i])
            self.M[i] = map(lambda x: x - minElem, self.M[i])

        # Now for column reduction
        for col in xrange(self.row):
            l = []
            for row in xrange(self.row):
                l.append(self.M[row][col])
            minElem = min(l)
            for row in xrange(self.row):
                self.M[row][col] -= minElem

    def getZeroPositions(self):
        """Returns current positions of 0's"""
        self.Z = set()
        for i in xrange(self.row):
            for j in xrange(self.row):
                if self.M[i][j] == 0:
                    self.Z.add((i, j))

    def printZeroLocations(self):
        print '\n Zeros are located at follows:',
        for i in self.Z:
            print i,
        print

    def checkAssignments(self):
        """What is the minimum assignment possible to cover all zeros"""

        bestComb = self.getSetOfCrossingLines()
        print '\n Current best combination to cover all zeros: ', len(bestComb)
        for i in bestComb:
            print '\t%s line through %s : %d' % (i.type, i.across, i.pos)

        curAssignments, totalVal = self.getAssignment(), 0
        print '\n  The assignments are as follows: \n',
        for i in curAssignments:
            x, y = i[0], i[1]
            print '\t At: ', x, y, ' Value: ',  _backup[x][y]
            totalVal += _backup[x][y]

        if len(bestComb) != self.row:
            # Perform the following steps
            print '\n Current solution isn\'t optimal: lines are not enough\n'
            self.tickRowsAndColumns(curAssignments)

        else:
            print '\n Current solution is optimal: Minimal cost: ', totalVal
            return

    def getDummy(self, n, m):
        """Add a dummy variable when rows != columns"""
        _m = max(n, m)
        for i in xrange(_m):
            for j in xrange(_m):
                self.M[i][j] = 0 if self.M[i][j] == -1 else self.M[i][j]
        return self.M

    def getSetOfCrossingLines(self):
        """Returns a set of lines that minimally cover all zeros"""

        horzLines = [HorzLine(i) for i in xrange(self.row)]
        vertLines = [VertLine(i) for i in xrange(self.row)]
        # We have to choose maximum n lines for crossing out all zeros
        # The assignment is optimal when the minimal lines are the order of the
        # matrix
        allComb = []
        for i in xrange(1, self.row + 1):
            allComb.extend(combinations(horzLines + vertLines, i))

        # Find the combination which covers the lists in the minimumLines
        bestComb = []

        for i in allComb:
            covered = set()
            for j in i:
                for zero in self.Z:
                    if zero in covered:
                        continue
                    elif j.type == 'Horizontal' and j.pos == zero[0]:
                        covered.add(zero)
                    elif j.type == 'Vertical' and j.pos == zero[1]:
                        covered.add(zero)
            if len(covered) == len(self.Z):
                if bestComb == []:
                    bestComb = i
                elif len(i) < len(bestComb):
                    bestComb = i

        return bestComb

    def getAssignment(self):
        """Asssign maximum number of zeroes possible """
        removedSet = set()

        # As there can be max n zeros
        bestAssign = set()

        # Since there are atleast 4 zeroes in our zeroes, array
        for comb in combinations(self.Z, self.row):
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

    def tickRowsAndColumns(self, assignments):
        """Tick rows and columns in the Matrix accordingly:
        - Tick rows that do not have an assignment
        - Tick cols that have 0's in the marked row
            - Tick all rows that have assignments in the marked column
            - Repeat the above procedure till no more can be ticked
            QuickThink: Use BFS and sets for row/cols
        """
        tickRows, tickCols = set(xrange(self.row)), set()
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
                for col in xrange(self.row):
                    if self.M[row][col] == 0:
                        tickCols.add(col)

            for col in tickCols:
                for assign in assignments:
                    if assign[1] == col and assign[0] not in tickRows:
                        tickRows.add(assign[0])
                        queue.append(assign[0])

        print '\n Ticked rows:  ', list(tickRows)
        print ' Ticked cols:  ', list(tickCols)

        # Draw straight lines through unmarked rows and marked columns
        horLines = [HorzLine(i) for i in xrange(self.row) if i not in tickRows]
        verLines = [VertLine(i) for i in xrange(self.row) if i in tickCols]
        bestComb = horLines + verLines

        print '\n Marking unmarked rows and marked cols:  ', len(bestComb)
        for i in bestComb:
            print '\t%s line through %s : %d' % (i.type, i.across, i.pos)

        if horLines + verLines == self.row:
            print '\n Current solution is optimal'
            curAssignments, totalVal = self.getAssignment(), 0
            print '\n  The assignments are as follows: \n',
            for i in curAssignments:
                x, y = i[0], i[1]
                print '\t At: ', x, y, ' Value: ',  _backup[x][y]
                totalVal += _backup[x][y]
            return True
        else:
            print '\n Current solution isn\'t optimal as lines are not enough'
            print ' Now going for uncovering elements pass'
            self.smallestElements(bestComb)
            self.getZeroPositions()
            print '\n New Zeros are located at follows:',
            for i in self.Z:
                print i,
            print
            self.checkAssignments()

    def smallestElements(self, bestComb):
        """
        Examine uncovered elements: Select min uncovered and subtract from all
        uncovered elements. For elements at intersection of two lines,
        add the min element, for rest : as it is
        """
        H_MASK, V_MASK, I_MASK = "H", "V", "I"
        MASK = [[None for i in xrange(self.row)] for j in xrange(self.row)]

        for line in bestComb:
            if line.type == "Horizontal":
                row = line.pos
                for col in xrange(self.row):
                    if MASK[row][col] is None:
                        MASK[row][col] = H_MASK
                    elif MASK[row][col] == V_MASK:
                        MASK[row][col] = I_MASK

            elif line.type == "Vertical":
                col = line.pos
                for row in xrange(self.row):
                    if MASK[row][col] is None:
                        MASK[row][col] = V_MASK
                    elif MASK[row][col] == H_MASK:
                        MASK[row][col] = I_MASK

        minElem = maxint
        for i in xrange(self.row):
            for j in xrange(self.row):
                if MASK[i][j] == None:
                    minElem = min(minElem, self.M[i][j])
        # Subtract min from uncovered, and add to intersection elems
        for i in xrange(self.row):
            for j in xrange(self.row):
                if MASK[i][j] == None:
                    self.M[i][j] -= minElem
                elif MASK[i][j] == I_MASK:
                    self.M[i][j] += minElem

        print '\n Uncovered matrix',
        self.printMatrix()


def readInput():
    """Read matrix from file and return a HungarianAssignment object"""
    solver = HungarianAssignment()

    if len(argv) != 2:
        print '\n No input file feeded'
        print ' Usage: python assignment.py "name_of_InputFile"'
        return solver

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

        solver.M = M
        if n != m:
            print '\n Matrices aren\'t of the same order'
            print ' Adding dummy\n'
            solver.getDummy(n, m)
        else:
            print '\n No dummy required'
        n = _m
        solver.row, solver.col = n, m

    except Exception as e:
        print '\n Exception occured: %s Check again' % (e)
    finally:
        return solver


if __name__ == '__main__':
    # Obtain matrix from file
    solver = readInput()
    if solver.M is None:
        print ' Error occured during execution\n'
        exit()
    _backup = solver.M[:]
    print '\n Matrix as in file:',
    solver.printMatrix()

    # Reduce the matrix
    solver.reduceMatrix()
    print '\n Reduced Matrix:',
    solver.printMatrix()

    # Get zero positions from the array
    solver.getZeroPositions()
    solver.printZeroLocations()

    # Check assignments
    solver.checkAssignments()
