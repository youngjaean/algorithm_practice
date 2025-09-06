def solution(nums, S):
    memo = {}
    def dp(index, target):
        if (index, target) in memo:
            return memo[(index, target)]
        if index == len(nums):
            return 1 if target == 0 else 0
        # The current number is added or subtracted
        result = dp(index + 1, target + nums[index]) + dp(index + 1, target - nums[index])
        memo[(index, target)] = result
        return result

    return dp(0, S)