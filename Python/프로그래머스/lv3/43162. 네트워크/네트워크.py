parent = {}


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root1 = find(x)
    root2 = find(y)

    if root1 != root2:
        if root1 < root2:
            parent[root2] = root1
        else:
            parent[root1] = root2


def solution(n, computers):
    for i in range(n):
        parent[i] = i

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j)

    for i in range(n):
        find(i)

    return len(set(parent.values()))