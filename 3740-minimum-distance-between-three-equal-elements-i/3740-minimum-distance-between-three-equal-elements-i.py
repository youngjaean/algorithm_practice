class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indexing = defaultdict(list)
        ans = float('inf')

        for i, num in enumerate(nums):
            indexing[num].append(i)
        
        for k, v in indexing.items():
            if len(v) >= 3:
                for i in range(0, len(v)-2):
                    ans = min(
                        ans,
                        abs(v[i] - v[i+1]) + abs(v[i+1] - v[i+2]) + abs(v[i+2] - v[i])
                    )
        if ans != float('inf') :
            return ans
        else:
            return -1