class Solution:
    def twoSum(self, nums: list, target):
        has_map = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in has_map:
                return [i, has_map[value]]
            has_map[nums[i]] = i
