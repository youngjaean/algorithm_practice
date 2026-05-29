class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_num = float("inf")

        for num in nums:
            tmp = 0

            while 10 <= num:
                value = num % 10
                num = num // 10
                tmp += value

            tmp += num

            min_num = min(min_num, tmp)

        return min_num