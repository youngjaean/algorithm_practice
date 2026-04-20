
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty, profit = map(list, zip(*sorted(zip(difficulty, profit))))
        answer = 0

        for w in worker:
            index = bisect_right(difficulty, w)
            if index > 0:
                answer += max(profit[:index])

        return answer