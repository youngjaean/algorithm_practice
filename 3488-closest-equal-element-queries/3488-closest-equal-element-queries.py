class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        num_index = defaultdict(list)
        for i, num in enumerate(nums):
            num_index[num].append(i)

        for pose in num_index.values():
            x = pose[0]
            pose.insert(0, pose[-1] - n)
            pose.append(x + n)

        for i in range(len(queries)):
            x = nums[queries[i]]
            pose_list = num_index[x]
            if len(pose_list) == 3:
                queries[i] = -1
                continue
            pose = bisect.bisect_left(pose_list, queries[i])

            queries[i] = min(
                pose_list[pose + 1] - pose_list[pose],
                pose_list[pose] - pose_list[pose - 1],
            )
        return queries
