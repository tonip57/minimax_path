import time
import math
import os
from collections import defaultdict
from collections import deque
INF = float('inf')

class DisjointSet:
    """
    Funktiot Kruskalin algoritmiin tarvittaville operaatioille
    """
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)
        
    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
            
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            seld.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[xroot] = yroot
            self.rank[xroot] += 1

class KruskalGraph:
    """
    Funktiot graafin luomiseen ja kutsu Dijkstran algoritmiin
    """
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []
        
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])
    
    def add_node(self, value):
        self.nodes.append(value)
        
    def callDijkstra(self, s, d, w):   
        
        dictionary = {}
        cities = 0
        for v in range(self.V):
            dictionary[v+1] = {}
            cities += 1
        
        for s, d, w in self.MST:               
            dictionary[d][s] = w
            dictionary[s][d] = w

        
        dijkstra(dictionary, 1, cities)        

            
    def kruskal(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.V - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.callDijkstra(s,d,w)


def dijkstra(graph,s,e):
    """
    Dijkstran algoritmi suoritetaan Kruskalin algoritmilla saadulle Minimum Spanning Tree:lle.
    """
    
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = INF
    path = []
    heightsList = []
    
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[s] = 0
    
    while unseenNodes:
        min_distance_node = None
        
        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node
                
        path_options = graph[min_distance_node].items()
        
        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node] 
                
                track_predecessor[child_node] = min_distance_node
                
        unseenNodes.pop(min_distance_node)
        
    currentNode = e
    heightsList.append(shortest_distance[e])
    while currentNode != s:
        try:
            path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
            heightsList.append(shortest_distance[currentNode])
            
        except KeyError:
            print("Reittiä ei ole")
            break
        
    path.insert(0, s)
    
    if shortest_distance[e] != infinity:
        
        previousItem = 0
        minus = 0
        answer = 0
        
        for item in heightsList:
            if item != heightsList[0]:
                minus = previousItem - item
                if minus > answer or answer == 0:
                    answer = minus
            previousItem = item
        
        printSolution(path, answer)

        
def printSolution(path,answer):
    """
    Tulostaa vastauksen
    """
    print("Matalin reitti: " + str(path))
    print("Reitin korkein kohta: " + str(answer))
    
    return
    
            
def main():
    """
    Main-funktiossa pyydetään käyttäjää syöttämään .txt tiedoston nimi, minkä jälkeen
    tiedostosta luetaan tieyhteydet KruskalGraphiin. Sen jälkeen lasketaan Kruskalin
    algoritmia käyttäen Minimum Spanning Tree.
    """
    fileName = ""
    last_line = 0
    
    #luetaan tiedostosta ensimmäinen ja viimeinen rivi
    fileName = input("Anna tiedoston nimi: ") 
    
    start_time = time.perf_counter()
    
    dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(dir, fileName)  
    with open(path) as f: 
        line = f.readline()
        for last_line in f:
            pass
    
    last_line = int(last_line)
    x = line.split()  
    cities = int(x[0])
    roads = int(x[1])
    
    g = KruskalGraph(cities)
    p = 1
    for f in range(cities):
        g.add_node(p)
        p += 1
    #luetaan tiedostosta tieyhteydet
    file = open(path)
    count = 0
    next(file)
    for line in file:
        if count < int(roads):
            y = line.split()
            g.add_edge(int(y[1]),int(y[0]),int(y[2]))
            g.add_edge(int(y[0]),int(y[1]),int(y[2]))
        count = count + 1

    start_time_alg = time.perf_counter()
    
    g.kruskal()
    end_time_alg = time.perf_counter() - start_time_alg
    end_time = time.perf_counter() - start_time
    
    print("Algoritmit suoritettu ajassa: " + str(end_time_alg))
    print("Kokonaisaika: " + str(end_time))
    
main()
