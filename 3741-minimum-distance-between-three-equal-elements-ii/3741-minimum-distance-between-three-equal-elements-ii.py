
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        check_dict = defaultdict(list)
        answer = float('inf')

        for idx, num in enumerate(nums):
            check_dict[num].append(idx)

        for key, value in check_dict.items():
            if len(value) >= 3:
                for i in range(len(value) - 2):
                    answer = min(
                        answer,
                        abs(value[i] - value[i+1]) +
                        abs(value[i+1] - value[i+2]) +
                        abs(value[i+2] - value[i])
                    )

        if answer != float('inf'):
            return answer
        else:
            return -1