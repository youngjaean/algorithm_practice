class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        if x == list(reversed(x)):
            return True
        else:
            return False
