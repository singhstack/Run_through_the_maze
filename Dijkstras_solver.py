def dijkstras(maze, start, end):
    # Get the number of rows and columns of the maze
    rows = len(maze)
    columns = len(maze[0])

    # Creating a dictionary containing the points in the maze and its neighbouring walls/cells in all directions
    map_dict = {}
    for i in range(rows):
        for j in range(columns):
            if i == 0:
                n_val = 0
            else:
                n_val = int(maze[i - 1][j])
            if j == 0:
                w_val = 0
            else:
                w_val = int(maze[i][j - 1])
            if j == columns - 1:
                e_val = 0
            else:
                e_val = int(maze[i][j + 1])
            if i == rows - 1:
                s_val = 0
            else:
                s_val = int(maze[i + 1][j])

            map_dict[(i, j)] = {'N': n_val, 'S': s_val, 'W': w_val, 'E': e_val}

    # Set the unvisited nodes to infinity while the start node would be 0
    unvisited = {n: float('inf') for n in map_dict.keys()}
    unvisited[start] = 0
    visited = {}

    # Create a dictionary for the final path
    final_path = {}

    # Check the closest point to the start point and assign the weights to them
    while unvisited:
        current = min(unvisited, key=unvisited.get)
        visited[current] = unvisited[current]
        if current == end:
            break
        for direction in 'NSWE':
            if map_dict[current][direction] == True:
                if direction == 'N':
                    previous = (current[0] - 1, current[1])
                if direction == 'S':
                    previous = (current[0] + 1, current[1])
                if direction == 'W':
                    previous = (current[0], current[1] - 1)
                if direction == 'E':
                    previous = (current[0], current[1] + 1)
                if previous in visited:
                    continue
                temp_val = unvisited[current] + 1

                if temp_val < unvisited[previous]:
                    unvisited[previous] = temp_val
                    final_path[previous] = current
        unvisited.pop(current)

    fwd_path = {}
    cell = end
    while cell != start:
        fwd_path[final_path[cell]] = cell
        cell = final_path[cell]

    # Create another maze to show the final paths
    dijkstra_maze = [[0 for i in range(columns)] for i in range(rows)]

    # Removing duplicates from all the nodes in the final path
    dijkstra_maze_path = list(set(list(fwd_path.keys()) + list(fwd_path.values())))

    # Based on the final graph create a new maze with only the solution to the maze
    for i in range(len(dijkstra_maze_path)):
        dijkstra_maze[dijkstra_maze_path[i][0]][dijkstra_maze_path[i][1]] = 1

    # Print the Maze
    #for line in dijkstra_maze:
    #    print(' '.join(map(str, line)))

def find_entry_exit(maze):
    start = 0,0
    end = 0,0
    # loop through the maze to find our start and end
    for i in range(0,len(maze)): #rows
        for j in range(0,len(maze[i])): #columns
            if i == 0:
                if maze[0][j] == 1:
                    start = i,j
            elif i == len(maze) - 1:
                if maze[len(maze) - 1][j] == 1:
                    end = i,j
    return start, end



