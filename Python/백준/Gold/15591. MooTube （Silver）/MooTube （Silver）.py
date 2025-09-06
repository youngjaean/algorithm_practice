def dfs(graph, start, weight_threshold):
    visited = [False] * (len(graph) + 1)
    stack = [start]
    count = 0

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            count += 1

            for neighbor, edge_weight in graph[node]:
                if not visited[neighbor] and edge_weight >= weight_threshold:
                    stack.append(neighbor)

    return count - 1


N, Q = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

results = []
for _ in range(Q):
    weight_threshold, start_node = map(int, input().split())
    result = dfs(graph, start_node, weight_threshold)
    results.append(result)

for result in results:
    print(result)
