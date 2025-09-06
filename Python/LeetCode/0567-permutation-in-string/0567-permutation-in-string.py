class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        cnt = Counter(s1)
        cnt_window = Counter(s2[:len_s1])

        if cnt == cnt_window:
            return True

        for i in range(len_s1, len_s2):
            cnt_window[s2[i]] += 1

            left_char = s2[i - len_s1]
            cnt_window[left_char] -= 1
            if cnt_window[left_char] == 0:
                del cnt_window[left_char]
            if cnt == cnt_window:
                return True

        return False