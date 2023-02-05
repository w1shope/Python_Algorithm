from collections import deque
import sys

def DFS(graph, v, visited) :
    visited[v] = True
    print(v, end = ' ')
    for tmp_v in graph[v] :
        if(visited[tmp_v] == False) :
            DFS(graph, tmp_v, visited)

def BFS(graph, v, visited) :
    queue = deque([v])
    while queue :
        tmp_v = queue.popleft()
        visited[tmp_v] = True
        print(tmp_v, end = ' ')
        for tmp_v2 in graph[tmp_v] :
            if(visited[tmp_v2] == False) :
                queue.append(tmp_v2)
                visited[tmp_v2] = True


N, M, K = map(int, sys.stdin.readline().split())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M) :
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    graph[v1].sort()
    graph[v2].sort()

DFS(graph, K, visited)
print()
visited = [False] * (N+1)
BFS(graph, K, visited)