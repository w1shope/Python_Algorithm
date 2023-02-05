import sys

def dfs(graph, start, visited) :
    visited[start] = 1

    for v in graph[start] :
        if(visited[v] == 0) :
            dfs(graph, v, visited)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M) :
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(graph, 1, visited)
print(sum(visited)-1)