class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        index_dic = defaultdict(list)
        answer = [0] * len(nums)
        for i, num in enumerate(nums):
            index_dic[num].append(i)
        
        for group in index_dic.values():
            total = sum(group)
            m = len(group)
            prefix_toal = 0
            for i, idx in enumerate(group):
                answer[idx] = total-prefix_toal * 2 + idx * (2 * i - m)
                prefix_toal += idx
        return answer