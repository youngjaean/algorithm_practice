class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        candidate = [i for i, v in enumerate(nums) if v == target]
        answer = float('inf')
        for con in candidate:
            answer = min(answer, abs(con - start))
        return answer