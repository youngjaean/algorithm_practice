class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        next_value = triangle[-1][:]
        current_value = [0] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                right_value = triangle[i][j] + next_value[j]
                left_value = triangle[i][j] + next_value[j + 1]
                current_value[j] = min(right_value, left_value)
            current_value, next_value = next_value, current_value
        return next_value[0]