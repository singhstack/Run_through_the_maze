from collections import deque
import copy

class DfsSolver():

    def __init__(self, maze) -> None:
        self.maze = maze

    # main function to solve the maze and return the result
    def SolveMaze(self):
        startRow, startCol = self.FindStart()
        return self.SolveDfs(startRow, startCol)

    # locate the start point at the top left part of the maze
    def FindStart(self):
        width = len(self.maze[0])
        height = len(self.maze)
        for column in range(0, width):
            # check top wall
            if (self.maze[0][column - 1] == 1):
                return 0, column - 1
                break
        for row in range(0, height):
            # check left wall
            if (self.maze[row][0] == 1):
                return row, 0
                break

    # #find all the possible next points from current point.
    # def find_next(self, row, col, maze):
    #     width = len(self.maze[0])
    #     height = len(self.maze)
    #     next_coordinates = []
    #     #check the upper point, row -1
    #     if row - 1 >= 0 and maze[row - 1][col] == 1:
    #         next_coordinates.append((row - 1, col))
    #     #check the right point, col + 1
    #     if col + 1 < width and maze[row][col + 1] == 1:
    #         next_coordinates.append((row, col + 1))
    #     #check the lower point, row + 1
    #     if row + 1 < height and maze[row + 1][col] == 1:
    #         next_coordinates.append((row + 1, col))
    #     #check the left point, col - 1
    #     if col - 1 >= 0 and maze[row][col - 1] == 1:
    #         next_coordinates.append((row, col - 1))
    #     return next_coordinates

    #solve the maze by using DFS
    def SolveDfs(self, startRow, startCol):
        width = len(self.maze[0])
        height = len(self.maze)
        #find end point
        for i in range(width - 1, -1, -1):
            if self.maze[height-1][i] == 1:
                endPoint = (height-1, i)
        # initiate the root of the search
        pointStack = []
        visited = []
        pointStack.append((startRow, startCol))
        visited.append((startRow, startCol))

        # travelsal the maze

        while pointStack and pointStack[-1] != endPoint:
            row, col = pointStack[-1][0],pointStack[-1][1]
            next_steps = []
            # check the upper point
            if row - 1 >= 0 and row - 1 < height:
                if self.maze[row - 1][col] == 1 and (row - 1, col) not in visited:
                    point = (row - 1, col)
                    # solution[point] = row, col
                    # currentPoints.append(point)
                    # visited.append(point)
                    next_steps.append(point)

            # check the right point
            if col + 1 >= 0 and col + 1 < width:
                if self.maze[row][col + 1] == 1 and (row, col + 1) not in visited:
                    point = (row, col + 1)
                    # solution[point] = row, col
                    # currentPoints.append(point)
                    # visited.append(point)
                    next_steps.append(point)

            # check the lower point
            if row + 1 >= 0 and row + 1 < height:
                if self.maze[row + 1][col] == 1 and (row + 1, col) not in visited:
                    point = (row + 1, col)
                    # solution[point] = row, col
                    # currentPoints.append(point)
                    # visited.append(point)
                    next_steps.append(point)

            # check the left point
            if col - 1 >= 0 and col - 1 < width:
                if self.maze[row][col - 1] == 1 and (row, col - 1) not in visited:
                    point = (row, col - 1)
                    # solution[point] = row, col
                    # currentPoints.append(point)
                    # visited.append(point)
                    next_steps.append(point)

            if len(next_steps) == 0:
                pointStack.pop()
                continue

            for p in next_steps:
                visited.append(p)
                pointStack.append(p)



        # track back the route to find solution
        # create a copy of the original maze to print our solution
        mazeSol = copy.deepcopy(self.maze)
        # while (row, col) != (startRow,startCol):
        #         mazeSol[row][col] = "x"  # replace the route by "x"
        #         row, col = solution[(row, col)]
        # mazeSol[startRow][startCol] = "x"  # replace the start point by "x"
        for e in pointStack:
            row, col = e[0], e[1]
            mazeSol[row][col] = "x"

        return mazeSol