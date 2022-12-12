# Run Through the Maze
CS5800
Tarandeep Singh, Anaelle Surprise, Man Fei Yau, Chen Yang

This project provides different algorithms to solve mazes with input maze size. 
## Dijkstras
This algorithm is generally used to find the shortest path between two vertices of a graph with a greedy approach. Briefly, it says that if we want to get from A to Z and that path goes via B and Y then the shortest path from A to Z also includes the shortest path from B to Y. It works by labeling the starting node as 0 and all the remaining nodes as infinity. It calculates the distance to adjacent nodes, selects the node with minimum distance and updates the node value to the distance it takes to reach them from the source.
## DFS
When looking at this problem in terms of Depth First Search, one would expect to go as far as they can until they cannot anymore. The nodes adjacent to walls in the case of the maze are like arriving at a leaf node. Depth First Search starts at the root, goes as far as it can, then would backtrack and this goes on until it arrives at the endpoint.
## BFS
Breadth First Search (BFS) is considered to be efficient because it searches all the branches at the same time. BFS begins at the root level and explores every node at the current level before heading over to the subsequent levels. If a solution is discovered, the algorithm will start to backtrack with the most efficient route and concludes the search. If it does not come across a solution not, it extends the node and resumes the search. 
## Maze Builder
We used Prim's algorithm to build our maze. Prim’s algorithm is a minimum spanning tree algorithm which we used to build random mazes. The maze we generate are perfect mazes i.e. there is only one path to go from start to exit. Prim’s approach starts from one point randomly and goes outward from that point.
## How to use
Simply run the main.py, and follow the instructions.
