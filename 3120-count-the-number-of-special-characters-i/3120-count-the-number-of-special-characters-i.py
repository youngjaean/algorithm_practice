class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        visited = []

        for i in range(len(word) - 1):
            for j in range(i + 1, len(word)):
                if (
                    abs(ord(word[i]) - ord(word[j])) == 32
                    and word[i] not in visited
                    and word[j] not in visited
                ):
                    count += 1
                    visited.extend([word[i], word[j]])
                    break

        return count