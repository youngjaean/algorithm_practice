from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        n, m = len(board), len(board[0])

        def dfs(x: int, y: int) -> None:
            stack = [(x, y)]
            board[x][y] = "S"

            while stack:
                x, y = stack.pop()

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "O":
                        board[nx][ny] = "S"
                        stack.append((nx, ny))

        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m - 1] == "O":
                dfs(i, m - 1)

        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j)
            if board[n - 1][j] == "O":
                dfs(n - 1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"