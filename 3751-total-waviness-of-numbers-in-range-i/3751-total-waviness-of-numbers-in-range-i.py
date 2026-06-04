class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0

        for i in range(num1, num2 + 1):
            s = str(i)

            for c in range(1, len(s) - 1):
                if (s[c - 1] < s[c] > s[c + 1]) or (s[c - 1] > s[c] < s[c + 1]):
                    total += 1

        return total