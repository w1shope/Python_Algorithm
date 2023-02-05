import sys

def dfs(start) :
    global count;
    visited[start] = True
    for i in range(1, N+1) :
        if(graph[start][i] == 1 and visited[i] == False) :
            count += 1
            dfs(i)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

for i in range(M) :
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

dfs(1)
print(count)