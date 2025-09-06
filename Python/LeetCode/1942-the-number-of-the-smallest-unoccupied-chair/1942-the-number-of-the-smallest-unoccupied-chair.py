class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arrives = []
        leaves = []
        for idx, (x, y) in enumerate(times):
            heapq.heappush(arrives, (x, idx))
            heapq.heappush(leaves, (y, idx))

        chair = [0] * len(times)
        while True:
            if arrives[0][0] < leaves[0][0]:
                arrive, idx = heapq.heappop(arrives)
                ans = chair.index(0)
                chair[ans] = 1
                if idx == targetFriend:
                    return ans
            else:
                leave, idx = heapq.heappop(leaves)
                chair[idx] = 0
