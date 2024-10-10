class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = 0
        closing = 0
        for ch in s:
            if ch == "(":
                opening += 1
            else:
                if opening:
                    opening -= 1
                else:
                    closing += 1

        return abs(len(opening) + closing)

