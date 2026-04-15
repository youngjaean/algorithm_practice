class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        answer = n = len(words) 
        for i , word in enumerate(words):
            if word == target:
                answer = min(answer, abs(i - startIndex), n - abs(i - startIndex))
        return answer if answer < n else -1