class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        answer = 0
        n = len(s)

        for i in range(n):
            freq = {}
            for j in range(i, n):
                c = s[j]
                freq[c] = freq.get(c, 0) + 1

                if freq[c] >= k:
                    answer += n - j
                    break

        return answer