class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_num = float("inf")

        for num in nums:
            digit_sum = sum(int(ch) for ch in str(num))
            min_num = min(min_num, digit_sum)

        return min_num