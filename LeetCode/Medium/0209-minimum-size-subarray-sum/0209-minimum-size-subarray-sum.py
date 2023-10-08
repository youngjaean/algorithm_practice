class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        can_ans = 0
        left = 0
        min_length = float("inf")
        for right in range(len(nums)):
            can_ans += nums[right]

            while can_ans >= target:
                min_length = min(min_length, right - left)
                can_ans -= nums[left]
                left += 1
        if min_length == float("inf"):
            return 0
        return min_length + 1