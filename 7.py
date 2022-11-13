class priorityqueue:
    def __init__(self) -> None:
        self.arr = []

    def lchild(self,pos) -> int:
        return (pos*2)+1

    def rchild(self,pos) -> int:
        return (pos*2)+2

    def parent(self,pos) -> int:
        return (pos-1)//2

    def isleaf(self,pos) -> bool:
        n = len(self.arr)
        return ((pos*2)>=n)

    def heapifyup(self,pos) -> None:
        while(pos>0):
            p = self.parent(pos)
            if self.arr[p] > self.arr[pos]:
                self.arr[p], self.arr[pos] = self.arr[pos], self.arr[p]
            pos = p
    
    def insert(self,ele) -> None:
        self.arr.append(ele)
        n =len(self.arr)
        if n==1:
            return
        self.heapifyup(n-1)

    def heapifydown(self, ind) -> None:
        if(self.isleaf(ind)):
            return
        n = len(self.arr)
        lc = self.lchild(ind)
        rc = self.rchild(ind)
        mini = ind
        if(lc<n and self.arr[lc]<self.arr[mini]):
            mini=lc
        if(rc<n and self.arr[rc]<self.arr[mini]):
            mini=rc
        if(mini != ind):
            self.arr[mini], self.arr[ind] = self.arr[ind], self.arr[mini]
            self.heapifydown(mini)


    def delete(self) -> None:
        # print(self.arr)
        t = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop(-1)
        self.heapifydown(0)
        return t

    def top(self) -> int:
        if len(self.arr) == 0:
            return
        else:
            return self.arr[0]

    def isempty(self) -> bool:
        n = len(self.arr)
        if n==0:
            return True
        else:
            return False





class graph :
    def __init__(self, vertices :int) -> None:
        self.v = vertices
        self.adj = [[] for _ in range(v)]
    
    def addedge(self, u : int, v : int, w : int) ->None:
        self.adj[u].append([v,w])
        self.adj[v].append([u,w])

    def shortestpath(self, src :int):
        pq = priorityqueue()
        dist = [int(1e9) for _ in range(self.v)]
        pq.insert([0,src])
        dist[src] = 0
        
        while not pq.isempty():
            u = pq.top()[1]
            pq.delete()
            for i in self.adj[u]:
                v = i[0]
                w = i[1]
                if dist[v] > dist[u]+w:
                    dist[v] = dist[u]+w
                    pq.insert([dist[v],v])
        print("/n")
        for i in range(self.v):
            print(f"The shortest distance form the {src} to {i} is {dist[i]}")

if __name__ == "__main__":
    v = int(input("Enter the number of vertices : "))
    g = graph(v)
    edges = int(input("Enter no edges : "))
    for i in range(edges):
        u = int(input("Enter vertex 1 : "))
        v = int(input("enter vertex 2 : "))
        w = int(input("enter weight : "))
        g.addedge(u,v,w)
    src = int(input("enter the vertex from which the shortest path should be calculated : "))
    g.shortestpath(src)
