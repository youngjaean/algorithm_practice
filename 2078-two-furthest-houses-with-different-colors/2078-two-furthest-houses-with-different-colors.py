class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        answer = 0
        for i, color in enumerate(colors):
            for j, col in enumerate(colors[i:], start=i):
                if color != col:
                    answer = max(answer, j - i)

        return answer
                    