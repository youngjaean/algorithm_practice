class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        while length < k:
            k -= length
        if length > 1 and k != 0:
            tmp = nums[-k:]
            nums[k - length :] = nums[0 : length - k]
            nums[0:k] = tmp