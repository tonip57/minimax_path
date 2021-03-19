# minimax_path
Solving minimax path problem using Kruskal's and Dijkstra's algorithms.

graph_ADS2018_2000.txt -file contains information about graph's vertices, edges, and weights. (Over 650 000 lines of text)

Weight = maximum height between two cities.

The problem was to find a route between city 1 and city 2000 where the maximum height between every pair of cities is as small as possible. (Not shortest path problem)

How I solved the problem:
1. I used Kruskal's algorithm to find out the minimum spanning tree of the graph.
2. Then I used Dijkstra's algorithm to find the route between city 1 and 2 while recording the maximum heights of the route.
