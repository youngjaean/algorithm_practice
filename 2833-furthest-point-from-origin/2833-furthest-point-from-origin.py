class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        move_con= Counter(moves)
        return abs(move_con["L"] - move_con["R"]) +move_con["_"]

    