class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        ans = []
        tmp = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                tmp.append(nums[i - 1])
                print(f"i:{i} tmp{tmp}")
            else:
                tmp.append(nums[i - 1])
                print(f"not continue i:{i} tmp{tmp}")

                if len(tmp) == 1:
                    ans.append(str(nums[i - 1]))
                else:
                    ans.append(f"{str(tmp[0])}->{str(tmp[-1])}")
                tmp = []
        tmp.append(nums[-1])
        if len(tmp) == 1:
            ans.append(str(tmp[0]))
        else:
            ans.append(f"{tmp[0]}->{tmp[-1]}")
        return ans
