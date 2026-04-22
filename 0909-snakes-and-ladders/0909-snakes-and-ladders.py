class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        vist = set([1])

        def gen_grid(pos):
            r, c = divmod(pos - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - c - 1
            return row, col

        queu = deque([(1, 0)])

        while queu:
            pos, move = queu.popleft()
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > n * n:
                    continue
                row, col = gen_grid(next_pos)

                if board[row][col] != -1:
                    next_pos = board[row][col]
                if next_pos == n*n:
                    return move + 1
                if next_pos not in vist:
                    vist.add(next_pos)
                    queu.append((next_pos, move + 1))

        return -1
