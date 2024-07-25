from collections import deque

def bfs_of_graph(V,adj):
    visited = [False]*V
    result = []
    queue = deque([0])

    visited[0] =True

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbour in adj[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
    return result

V1 = 5
E1 = 4
adj1 = [[1,2,3],[],[4],[],[]]
print(bfs_of_graph(V1, adj1))  
V2 = 3
E2 = 2
adj2 = [[1,2],[],[]]
print(bfs_of_graph(V2, adj2))