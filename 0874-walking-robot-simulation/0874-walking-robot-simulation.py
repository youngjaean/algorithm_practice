from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = 0 
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        x, y = 0, 0
        obstacle_set = set(map(tuple, obstacles))
        max_dist = 0

        for com in commands:
            if com == -1:
                direction = (direction + 1) % 4
            elif com == -2:
                direction = (direction + 3) % 4
            else:
                for _ in range(com):
                    nx = x + dx[direction]
                    ny = y + dy[direction]

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)

        return max_dist