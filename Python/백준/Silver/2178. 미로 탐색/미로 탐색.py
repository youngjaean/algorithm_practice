from collections import deque
def bfs(graph):
    node = deque([[0,0]])
    rx = [0,1,0,-1]
    ry = [1,0,-1,0]
    visted =[[0,0]]
    while  node:
        next_node = node.popleft()
        for x, y in zip(rx, ry):
            if next_node[0] + x >= 0 and next_node[0] + x < len(graph) and next_node[1] + y >=0 and next_node[1] + y < len(graph[0]) and graph[next_node[0] + x][next_node[1] + y] != 0:
                if [next_node[0] + x, next_node[1]+y] not in visted:
                    node.append([next_node[0] + x, next_node[1]+y])
                    visted.append([next_node[0] + x, next_node[1]+y])     
                    graph[next_node[0] + x][next_node[1]+y] += graph[next_node[0]][next_node[1]]
   
    print(graph[-1][-1])

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
bfs(graph)

