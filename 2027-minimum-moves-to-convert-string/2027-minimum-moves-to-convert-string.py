class Solution:
    def minimumMoves(self, s: str) -> int:
        change = 0
        i  = 0
        while len(s) > i:
            if s[i] !=  "O":
                chunk = s[i : i + 3]
                change += 1
                i += 3
            else:
                i+=1

        return change
