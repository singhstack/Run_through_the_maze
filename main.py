from maze_builder import build, printmaze
from maze_solver import dijkstras, find_entry_exit
from BFS_solver import BfsSolver
from DFS_solver import DfsSolver
import timeit


timings_maze10 = {'dijk':[], 'bfs':[],'dfs':[],'backtracking':[]}
timings_maze50 = {'dijk':[], 'bfs':[],'dfs':[],'backtracking':[]}
timings_maze100 = {'dijk':[], 'bfs':[],'dfs':[],'backtracking':[]}
dim = [10,50,100]
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
        elif d==50:
            timings_maze50['dijk'].append(elapsed)
        elif d==100:
            timings_maze100['dijk'].append(elapsed)
        #BFS
        start_time2 = timeit.default_timer()
        bfs = BfsSolver(m)
        elapsed = timeit.default_timer() - start_time2
        if d==10:
            timings_maze10['bfs'].append(elapsed)
        elif d==50:
            timings_maze50['bfs'].append(elapsed)
        elif d==100:
            timings_maze100['bfs'].append(elapsed)

        #DFS
        start_time3 = timeit.default_timer()
        dfs = DfsSolver(m)
        elapsed = timeit.default_timer() - start_time3
        if d==10:
            timings_maze10['dfs'].append(elapsed)
        elif d==50:
            timings_maze50['dfs'].append(elapsed)
        elif d==100:
            timings_maze100['dfs'].append(elapsed)

        #Backtracking

print("Dijks run time")
print(round(sum(timings_maze10['dijk'])/len(timings_maze10['dijk'])*1000,2))
print(round(sum(timings_maze50['dijk'])/len(timings_maze50['dijk'])*1000,2))
print(round(sum(timings_maze100['dijk'])/len(timings_maze100['dijk'])*1000,2))
print("BFS run time")
print(round(sum(timings_maze10['bfs'])/len(timings_maze10['bfs'])*1000,2))
print(round(sum(timings_maze50['bfs'])/len(timings_maze50['bfs'])*1000,2))
print(round(sum(timings_maze100['bfs'])/len(timings_maze100['bfs'])*1000,2))
print("DFS run time")
print(round(sum(timings_maze10['dfs'])/len(timings_maze10['dfs'])*1000,2))
print(round(sum(timings_maze50['dfs'])/len(timings_maze50['dfs'])*1000,2))
print(round(sum(timings_maze100['dfs'])/len(timings_maze100['dfs'])*1000,2))

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
