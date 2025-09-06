import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r"[^a-z0-9]", "", s)
        s_2 = list(reversed(s))
        if s_2 == list(s):
            return True
        else:
            return False