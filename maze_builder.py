def build(height,width):
    import random
    #cell/path denoted by  1
    #wall denoted by 0

    def initialise_maze(height, width):
        maze = [['u' for i in range(width)] for j in range(height)]
        return maze

    # helper function to build entry and exit points of the maze
    def built_entry_exit_points(maze, width, height):
        for i in range(0, width):
            if (maze[1][i] == 1):
                maze[0][i] = 1
                break
        for i in range(width - 1, 0, -1):
            if (maze[height - 2][i] == 1):
                maze[height - 1][i] = 1
                break
        return maze

    maze = initialise_maze(height,width)

    random_height = int(random.random() * height)#range is from 1 to height-1 to make sure it does
    random_width = int(random.random() * width)  #not start on the edge of the maze
    if (random_height == 0):
        random_height += 1
    if (random_height == height - 1):
        random_height -= 1
    if (random_width == 0):
        random_width += 1
    if (random_width == width - 1):
        random_width -= 1

    maze[random_height][random_width] = 1
    #add the surrounding walls to the queue
    walls = []
    walls.append([random_height+1,random_width])
    walls.append([random_height,random_width+1])
    walls.append([random_height,random_width-1])
    walls.append([random_height-1,random_width])

    maze[random_height+1][random_width] = 0
    maze[random_height][random_width+1] = 0
    maze[random_height][random_width-1] = 0
    maze[random_height-1][random_width] = 0

    #helper function to find out how many surrounding cells we have
    def surroundingCells(rand_wall):
        s_cells = 0
        if (maze[rand_wall[0]-1][rand_wall[1]] == 1):
            s_cells += 1
        if (maze[rand_wall[0]+1][rand_wall[1]] == 1):
            s_cells += 1
        if (maze[rand_wall[0]][rand_wall[1]-1] == 1):
            s_cells +=1
        if (maze[rand_wall[0]][rand_wall[1]+1] == 1):
            s_cells += 1
        return s_cells
    #this function will help us keep the maze restricted and clean - no wall about to be converted should
    # have more than 1 cell around it



    #choosing a random wall
    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == 1):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != 1):
                            maze[rand_wall[0] - 1][rand_wall[1]] = 0
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Bottom cell
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != 1):
                            maze[rand_wall[0] + 1][rand_wall[1]] = 0
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != 1):
                            maze[rand_wall[0]][rand_wall[1] - 1] = 0
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == 1):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != 1):
                            maze[rand_wall[0] - 1][rand_wall[1]] = 0
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != 1):
                            maze[rand_wall[0]][rand_wall[1] - 1] = 0
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Rightmost cell
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != 1):
                            maze[rand_wall[0]][rand_wall[1] + 1] = 0
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if (rand_wall[0] != height - 1):
            if (maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] - 1][rand_wall[1]] == 1):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark the new walls
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != 1):
                            maze[rand_wall[0] + 1][rand_wall[1]] = 0
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1] - 1] != 1):
                            maze[rand_wall[0]][rand_wall[1] - 1] = 0
                        if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != 1):
                            maze[rand_wall[0]][rand_wall[1] + 1] = 0
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the right wall
        if (rand_wall[1] != width - 1):
            if (maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == 1):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 1

                    # Mark the new walls
                    if (rand_wall[1] != width - 1):
                        if (maze[rand_wall[0]][rand_wall[1] + 1] != 1):
                            maze[rand_wall[0]][rand_wall[1] + 1] = 0
                        if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if (rand_wall[0] != height - 1):
                        if (maze[rand_wall[0] + 1][rand_wall[1]] != 1):
                            maze[rand_wall[0] + 1][rand_wall[1]] = 0
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0] - 1][rand_wall[1]] != 1):
                            maze[rand_wall[0] - 1][rand_wall[1]] = 0
                        if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)

    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = 0
    maze = built_entry_exit_points(maze,width,height)
    return maze

def printmaze(maze):
    for i in range(len(maze)):
        string=""
        for j in range(len(maze[0])):
            string+=str(maze[i][j])
            string+=" "

        print(string)
'''
maze = build(height=10, width=6)
printmaze(maze)'''






