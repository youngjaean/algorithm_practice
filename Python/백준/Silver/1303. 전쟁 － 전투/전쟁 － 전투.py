from collections import deque


def bfs(graph, visited, start, c):
    dx = [0, -1, 1, 0]
    dy = [1, 0, 0, -1]
    cnt = 1
    node = deque([start])
    visited[start[0]][start[1]] = True
    while node:
        x, y = node.popleft()
        for nx, ny in zip(dx, dy):
            X = nx + x
            Y = ny + y
            if (
                0 <= X < len(graph)
                and 0 <= Y < len(graph[0])
                and visited[X][Y] != True
                and graph[X][Y] == c
            ):
                visited[X][Y] = True
                cnt += 1
                node.append((X, Y))
    return cnt, visited


n, m = map(int, input().split())
visited = [[False] * n for _ in range(m)]
graph = [list(input().rstrip()) for _ in range(m)]
w_cnt = 0
b_cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == "W" and visited[i][j] != True:
            w_tmp, visited = bfs(graph, visited, [i, j], "W")
            w_cnt += w_tmp**2
        elif graph[i][j] == "B" and visited[i][j] != True:
            b_tmp, visited = bfs(graph, visited, [i, j], "B")
            b_cnt += b_tmp**2

print(w_cnt, b_cnt)
