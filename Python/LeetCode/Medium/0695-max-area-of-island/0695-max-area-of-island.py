class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.n, self.m = len(grid), len(grid[0])
        self.grid = grid
        self.visted = []
        answer = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] != 0 and [i, j] not in self.visted:
                    answer = max(answer, self.bfs(i, j))
        return answer

    def bfs(self, i, j):
        count = 1
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        node = deque([[i, j]])
        self.visted.append([i, j])
        while node:
            x_node, y_node = node.popleft()
            for x, y in zip(dx, dy):
                nx, ny = x_node + x, y_node + y
                if (
                    0 <= nx < self.n
                    and 0 <= ny < self.m
                    and [nx, ny] not in self.visted
                    and self.grid[nx][ny] == 1
                ):
                    node.append([nx, ny])
                    self.visted.append([nx, ny])
                    count += 1
        return count