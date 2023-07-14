from collections import deque


def bfs(graph, start):
    print(start, end=" ")
    visted = [start]
    nodes = deque([start])
    values = []
    while nodes:
        next_node = nodes.popleft()
        visted.append(next_node)
        if next_node in graph.keys():
            for next_value in graph[next_node]:
                if next_value not in visted:
                    values.append(next_value)
                    # print(next_value, end=" ")
                    visted.append(next_value)
                    nodes.append(next_value)
    print(*values)


def dfs(graph, start, visted):
    print(start, end=" ")
    if start in graph.keys():
        for next_node in graph[start]:
            if next_node not in visted:
                visted.append(next_node)
                dfs(graph, next_node, visted)


N, M, start = map(int, input().split())
graph = {0: [0]}
for _ in range(M):
    key, value = map(int, input().split())
    try:
        graph[key].append(value)
    except:
        graph[key] = [value]
    try:
        graph[value].append(key)
    except:
        graph[value] = [key]
for value in graph.values():
    value.sort()
visted = [start]
dfs(graph, start, visted)
print()
bfs(graph, start)
