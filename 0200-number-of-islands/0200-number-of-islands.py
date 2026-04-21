class Solution:
    def BFS(self, start, grid):
        queue = deque([start])
        grid[start[0]][start[1]] = "0"
        while queue:
            x, y = queue.popleft()
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    queue.append([nx, ny])

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.BFS([i, j], grid)
                    ans += 1

        return ans