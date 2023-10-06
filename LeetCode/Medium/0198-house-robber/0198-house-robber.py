class Solution:
    def rob(self, nums: List[int]) -> int:        
        if len(nums) <= 2:
            return max(nums)

        L = len(nums)
        value, answer_value = nums[0], max(nums[0], nums[1])

        for i in range(2, L):
            value, answer_value = answer_value, max(value + nums[i], answer_value)

        return answer_value