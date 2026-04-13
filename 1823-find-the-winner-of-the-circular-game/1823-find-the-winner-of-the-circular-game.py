class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        index = 0
        candidates = [i for i in range(1, n + 1)]  # 보통 1-based
        
        while len(candidates) > 1:
            index = (index + k - 1) % len(candidates)
            candidates.pop(index)
        
        return candidates[0]