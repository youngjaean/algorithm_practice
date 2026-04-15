class Solution:
    def minTimeToType(self, word: str) -> int:
        pointer = 'a'
        answer = 0

        for char in word:
            diff = abs(ord(char) - ord(pointer))
            answer += min(diff, 26 - diff) + 1
            pointer = char

        return answer