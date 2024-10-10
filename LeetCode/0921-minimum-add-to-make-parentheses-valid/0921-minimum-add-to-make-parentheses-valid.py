class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = []
        closing = 0
        for ch in s:
            if ch == "(":
                opening.append(ch)
            else:
                if opening:
                    opening.pop()
                else:
                    closing += 1

        return abs(len(opening) + closing)

