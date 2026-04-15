
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0

        for i in range(n - 2):
            for j in range(m - 2):
                sum_value = 0
                for di in range(3):
                    for dj in range(3):
                        if di == 1 and dj != 1:
                            continue
                        sum_value += grid[i + di][j + dj]

                ans = max(ans, sum_value)

        return ans
