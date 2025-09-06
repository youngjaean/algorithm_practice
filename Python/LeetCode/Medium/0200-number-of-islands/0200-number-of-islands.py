class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        m, n = len(grid), len(grid[0])
        num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    node = deque([[i, j]])
                    grid[i][j] = "2"

                    while node:
                        nx, ny = node.popleft()
                        for x, y in zip(dx, dy):
                            if (
                                0 <= nx + x < m
                                and 0 <= ny + y < n
                                and grid[nx + x][ny + y] == "1"
                            ):
                                node.append([nx + x, ny + y])
                                grid[nx + x][ny + y] = "2"
                    num += 1
        return num