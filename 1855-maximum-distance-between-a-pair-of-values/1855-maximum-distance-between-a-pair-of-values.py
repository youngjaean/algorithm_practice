from typing import List

class Solution:
    def binary_search(self, left, right, nums, target):
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        answ = 0

        for i, num1 in enumerate(nums1):
            pos = self.binary_search(i, len(nums2) - 1, nums2, num1)
            if pos != -1:
                answ = max(answ, pos - i)

        return answ