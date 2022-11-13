# Importing the priority_queue code
from priority_queue import priority_queue

class Graph:
    # constructor
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    # adding edges
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

# Functiion to calculate the shortest path from a given source vertex
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(graph.v)}
    D[start_vertex] = 0

    # list used to calculate the path
    child = [-1 for i in range(graph.v)]

    # Invoking priority queue functions
    pq = priority_queue(key=lambda x: x[1])
    pq.heap_push((start_vertex,0))

    while not pq.empty():
        (current_vertex,dist) = pq.top()
        pq.heap_pop()
        # We put the start vertex in the priority queue. Now, for each vertex in the priority queue, we will first mark them as visited, and then we will iterate through their neighbors.
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                # If the neighbor is not visited, we will compare its old cost and its new cost
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    # f the new cost is lower than the old cost, we put the neighbor and its cost to the priority queue, and update the list where we keep the shortest paths accordingly.
                    if new_cost < old_cost:
                        pq.heap_push((neighbor,new_cost))
                        D[neighbor] = new_cost
                        child[current_vertex] = graph.edges[0][neighbor]
    return D,child

# Function to print the path taken from source to destination
def print_path(c,src,des):
    def printPathUntil(c,curr,target):
        if(curr == c[curr] or curr == target):
            return
        print(curr,end="->")
        printPathUntil(c,c[curr],target)
    printPathUntil(c,src,des)
    print(des)

# Driver code
if __name__ == "__main__":
    # graph taken
    # g = Graph(9)
    # g.add_edge(0, 1, 4)
    # g.add_edge(0, 6, 7)
    # g.add_edge(1, 6, 11)
    # g.add_edge(1, 7, 20)
    # g.add_edge(1, 2, 9)
    # g.add_edge(2, 3, 6)
    # g.add_edge(2, 4, 2)
    # g.add_edge(3, 4, 10)
    # g.add_edge(3, 5, 5)
    # g.add_edge(4, 5, 15)
    # g.add_edge(4, 7, 1)
    # g.add_edge(4, 8, 5)
    # g.add_edge(5, 8, 12)
    # g.add_edge(6, 7, 1)
    # g.add_edge(7, 8, 3) 

    v = int(input("Enter No of vertices : "))
    g = Graph(v)
    E = int(input("Enter No of Edges : "))
    
    for _ in range(E):
        print(f"For Edge {_+1}: ")
        u,v,w = map(int,input("\tEnter u,v,w seperated by spaces : ").split())
        g.add_edge(u,v,w)

    source = int(input("Enter the source vertex : "))
    Dest = int(input("Enter the Destination vertex : "))

    c=[]

    D,c = dijkstra(g, source)

    print("Distance from vertex 0 to vertex", Dest, "is", D[Dest])

    print("Using the path : ",end=" ")
    print_path(c,source,Dest)