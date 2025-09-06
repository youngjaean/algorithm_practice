class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = 0
        for i, c in enumerate(s):
            n = n * int(c) if c.isdigit() else n + 1
            if k <= n:
                break

        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                n /= int(c)
                k %= n
            else:
                if k == n or k == 0:
                    return c
                n -= 1