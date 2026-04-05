class Solution:
    def judgeCircle(self, moves: str) -> bool:
        col, row = 0, 0
        for move in moves:
            if move == "U":
                col -= 1
            elif move == "D":
                col += 1
            elif move == "R":
                row -= 1
            elif move == "L":
                row += 1
        
        return col == 0 and row == 0
