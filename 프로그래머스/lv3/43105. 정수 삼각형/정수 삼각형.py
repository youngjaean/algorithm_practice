def max_value(triangle, i, j, visited):
    if i + 1 == len(triangle):
        return triangle[i][j]
    if (i, j) in visited:
        return visited[(i, j)]
    right = max_value(triangle, i + 1, j, visited)
    left = max_value(triangle, i + 1, j + 1, visited)
    x = triangle[i][j] + max(right, left)

    visited[(i, j)] = x
    return x


def solution(triangle):
    visited = {}
    return max_value(triangle, 0, 0, visited)