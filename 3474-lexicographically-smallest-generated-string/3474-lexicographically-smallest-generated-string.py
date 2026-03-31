class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        answer = ["a"] * (n + m - 1)
        factor = [False] * (n + m - 1)

        for i, ch in enumerate(str1):
            if ch == "T":
                for j, c in enumerate(str2, i):
                    if factor[j] and answer[j] != c:
                        return ""
                    answer[j], factor[j] = c, True

        for i, ch in enumerate(str1):
            if ch == "F":
                if any(str2[j - i] != answer[j] for j in range(i, i+m)):
                    continue

                for j in range(i + m - 1, i -1, -1):
                    if not factor[j]:
                        answer[j] = "b"
                        break

                else:
                    return ""

        return "".join(answer)
