from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        n, m = len(board), len(board[0])
        visited = set()

        for X in range(n):
            for Y in range(m):
                if board[X][Y] == "O" and (X, Y) not in visited:
                    check = True
                    change = []
                    stack = [(X, Y)]
                    visited.add((X, Y))

                    while stack:
                        x, y = stack.pop()
                        change.append((x, y))

                        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                            check = False

                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx = x + dx
                            ny = y + dy

                            if (
                                0 <= nx < n
                                and 0 <= ny < m
                                and board[nx][ny] == "O"
                                and (nx, ny) not in visited
                            ):
                                visited.add((nx, ny))
                                stack.append((nx, ny))

                    if check:
                        for x, y in change:
                            board[x][y] = "X"