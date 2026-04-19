

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        answ = 0
        nums2 = [-x for x in nums2]
        for i, num1 in enumerate(nums1):
            pos = bisect.bisect_right(nums2, -num1)
            if i <= pos:
                answ = max(answ, pos - i - 1)

        return answ
