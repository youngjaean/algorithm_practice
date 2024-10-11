class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = Counter(s1)

        for i in range(len(s2)):
            cnt_s2 = Counter(s2[i : i + len(s1)])

            if cnt == cnt_s2:
                return True

        return False

