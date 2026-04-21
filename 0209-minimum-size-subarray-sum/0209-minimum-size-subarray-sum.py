class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = len(nums) + 1
        left = 0
        value = 0

        for right in range(len(nums)):
            value += nums[right]

            while value >= target:
                min_length = min(min_length, right - left + 1)
                value -= nums[left]
                left += 1

        return 0 if min_length == len(nums) + 1 else min_length