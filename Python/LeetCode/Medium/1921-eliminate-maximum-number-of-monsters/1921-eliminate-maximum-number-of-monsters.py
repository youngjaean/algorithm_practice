class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        for i, t in enumerate(sorted((d + s - 1) // s for d, s in zip(dist, speed))):
            if i == t:
                return i
        return len(dist)
