from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    distance = [-1] * (n + 1)
    distance[1] = 0

    queue = deque([1])
    visited[1] = True

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    max_distance = max(distance)
    return distance.count(max_distance)