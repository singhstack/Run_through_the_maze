from maze_builder import build, printmaze
from maze_solver import dijkstras, find_entry_exit
import timeit


timings_maze10 = {'dijk':[], 'bfs':[],'dfs':[],'backtracking':[]}
timings_maze30 = {'dijk':[], 'bfs':[],'dfs':[],'backtracking':[]}
timings_maze50 = {'dijk':[], 'bfs':[],'dfs':[],'backtracking':[]}
dim = [10,30,50]
iterations = 50
for d in dim:
    for i in range(iterations):
        m = build(d, d)
        start, end = find_entry_exit(m)
        #Dijkstras
        start_time = timeit.default_timer()
        dijkstras(m, start, end)
        elapsed = timeit.default_timer() - start_time
        if d==10:
            timings_maze10['dijk'].append(elapsed)
        elif d==30:
            timings_maze30['dijk'].append(elapsed)
        elif d==50:
            timings_maze50['dijk'].append(elapsed)
        #BFS

        #DFS

        #Backtracking

print(round(sum(timings_maze10['dijk'])/len(timings_maze10['dijk'])*1000,2))
print(round(sum(timings_maze30['dijk'])/len(timings_maze30['dijk'])*1000,2))
print(round(sum(timings_maze50['dijk'])/len(timings_maze50['dijk'])*1000,2))




'''
def __init__main():
    print("Press Y to build a maze: ")
    print("Enter height: ")
    print("Enter width: ")
    build(height,width)
    print("Your maze has been built.")

    Print("Which Algorithm would you like to use to solve the maze")

    Djiks


'''