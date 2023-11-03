class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = s[0]
        self.s = s
        length = len(s)
        for i in range(len(s) - 1):
            odd = self.comput_length(i, i, length)
            even = self.comput_length(i, i + 1, length)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str

    def comput_length(self, left, right, length):
        while left >= 0 and right < length and self.s[left] == self.s[right]:
            left -= 1
            right += 1
        return self.s[left + 1 : right]
