from collections import deque
import copy

class BfsSolver():
    
    def __init__(self, maze) -> None:
        self.maze = maze

    # main function to solve the maze and return the result
    def SolveMaze(self):
        startRow, startCol = self.FindStart()
        return self.SolveBfs(startRow, startCol)


    # locate the start point
    # we assume start point located on the top wall or the left wall
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

    #solve the maze by using BFS
    def SolveBfs(self, startRow, startCol):
        # initiate the root of the search
        currentPoints = deque()
        solution = {}
        visited = []
        currentPoints.append((startRow, startCol))
        solution[(startRow, startCol)] = startRow,startCol
        visited.append((startRow, startCol))

        # travelsal the maze
        width = len(self.maze[0])
        height = len(self.maze)
        while len(currentPoints) > 0:
            row, col = currentPoints.popleft()

            #check the left point
            if col - 1 >= 0 and col -1 < width:
                if self.maze[row][col-1] == 1 and (row, col-1) not in visited:
                    point = (row, col-1)
                    solution[point] = row,col
                    currentPoints.append(point)
                    visited.append(point)
            # check the right point
            if col + 1 >= 0 and col + 1 < width:
                if self.maze[row][col+1] == 1 and (row, col+1) not in visited:
                    point = (row, col+1)
                    solution[point] = row,col
                    currentPoints.append(point)
                    visited.append(point)
            # check the upper point
            if row - 1 >= 0 and row - 1 < height:
                if self.maze[row-1][col] == 1 and (row-1, col) not in visited:
                    point = (row-1, col)
                    solution[point] = row,col
                    currentPoints.append(point)
                    visited.append(point)
            # check the lower point
            if row + 1 >= 0 and row + 1 < height:
                if self.maze[row+1][col] == 1 and (row+1, col) not in visited:
                    point = (row+1, col)
                    solution[point] = row,col
                    currentPoints.append(point)
                    visited.append(point)

        # track back the route to find solution
        # create a copy of the original maze to print our solution
        mazeSol = copy.deepcopy(self.maze)
        while (row, col) != (startRow,startCol):
                mazeSol[row][col] = "x"  # replace the route by "x"
                row, col = solution[(row, col)]
        mazeSol[startRow][startCol] = "x"  # replace the start point by "x"
        return mazeSol
                
            
