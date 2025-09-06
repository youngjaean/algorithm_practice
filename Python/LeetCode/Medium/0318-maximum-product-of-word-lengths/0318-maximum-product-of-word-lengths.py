class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def common(char1, char2):
            for c1 in char1:
                if c1 in char2:
                    return False
            return True

        ans = 0
        for i in range(len(words)):
            for ch2 in words[i:]:
                if common(words[i], ch2):
                    ans = max(ans, len(words[i]) * len(ch2))

        return ans
