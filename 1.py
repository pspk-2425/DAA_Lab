class Graph:
    def __init__(self,no_of_vertices):
        self.v = no_of_vertices
        self.graph = {}
    
    def addEdge(self,u,v):
        self.graph[u].append(v)


def bfs(g,start):
    visited = {key : False for key in g.graph}
    queue = []
    queue.append(start)
    visited[start] = True
    i=0
    while(queue and i < 2):
        n = len(queue)
        while(n):
            for frnd in g.graph[queue[0]]:
                if visited[frnd] == False:
                    queue.append(frnd)
                    visited[frnd] = True
            queue.pop(0)
            n-=1
        i+=1
    print(queue)


if __name__ == "__main__":
    n = int(input("Enter no of vertices : "))
    g = Graph(n)
    for i in range(n):
        user = input(f"Enter the name of user{i+1} :")
        g.graph[user] = []

    for key in g.graph:
        print("\n user-> "+key)
        #inputting all the friends of current user
        k = int(input(f"Enter the no of friends of {key}: ")) 
        for i in range(k):
            name = input(f"\tenter the name of the friend {i+1} :")
            g.addEdge(key,name)

    user_bfs = input("Enter the name of the user for friend suggestions : ")
    bfs(g,user_bfs)

# g.addEdge(1, 2)
# g.addEdge(1, 3)
# g.addEdge(2, 1)
# g.addEdge(2, 4)
# g.addEdge(3, 1)
# g.addEdge(3, 4)
# g.addEdge(3, 6)
# g.addEdge(4, 2)
# g.addEdge(4, 3)
# g.addEdge(4, 5)
# g.addEdge(5, 4)
# g.addEdge(6, 3)
# print(g.graph)g = Graph(6)

# bfs(g,1)
# bfs(g,2)
# bfs(g,3)
# bfs(g,4)
# bfs(g,5)
# bfs(g,6)
                

