n = int(input("Enter no of users : \n"))
graph = {}
for i in range(n):
    name = input("Enter the name of user "+ str(i+1) + " : \n")
    graph[name] = []

for key in graph:
    print("for user"+ key + "\n")
    n = int(input("enter no of friends: \n"))
    for i in range(n):
        name = input("enter the name of the friend "+ str(i+1) + " : \n")
        graph[key].append(name)

def bfs(graph, start):
    visited = {key:False for key in graph}
    queue = []
    i = 0 
    queue.append(start)
    visited[start] = True
    while queue and i<2:
        n = len(queue)
        while(n):
            for frnd in graph[queue[0]]:
                if visited[frnd] == False:
                    queue.append(frnd)
                    visited[frnd] = True
            queue.pop(0)
            n-=1
        i+=1
    print("friend suggestions for the user "+ start)
    print(queue)

user = input("Enter the name of the user for friend suggestions : \n")
bfs(graph,user)