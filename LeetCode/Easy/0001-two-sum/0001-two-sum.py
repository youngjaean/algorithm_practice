class Solution:
    def twoSum(self, nums: list, target):
        # nums.sort()
        result = []
        while nums:
            index = -1
            try:
                index = nums.index(target - nums.pop())
            except:
                pass
            if index != -1:
                result = [index, len(nums)]
                # nums.pop(index)
                break

        return result
