class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(x) for x in ''.join(map(str, nums))]