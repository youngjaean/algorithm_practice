class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def change_time(time):
            hour, mim = map(int, time.split(":"))

            return hour * 60 + mim

        new_time = [change_time(time) for time in timePoints]

        new_time.sort()
        ans = float("inf")
        for nt, nnt in zip(new_time[:-1], new_time[1:]):
            ans = min(ans, abs(nt - nnt))

        mid_night = 1440 - new_time[-1] + new_time[0]

        return min(ans, mid_night)
