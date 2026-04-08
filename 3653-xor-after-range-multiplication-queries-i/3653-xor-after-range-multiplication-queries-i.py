class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        for querie in queries:
            for idx in range(querie[0], querie[1] + 1, querie[2]):
                nums[idx] = (nums[idx] * querie[3]) % (10**9 + 7)
        result = 0
        for x in nums:
            result ^= x
        return result