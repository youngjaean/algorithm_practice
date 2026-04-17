class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        position_dic = defaultdict(list)
        distance = float("inf")

        for i, num in enumerate(nums):
            position_dic[num].append(i)

        for i, num in enumerate(nums):
            reverse = int(str(num)[::-1])
            value = position_dic.get(reverse, [])

            j = bisect_right(value, i)
            if j < len(value):
                distance = min(distance, value[j] - i)

        return -1 if distance == float("inf") else distance