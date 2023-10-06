class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(s, wordDict, answer={}):
            if s in answer:
                return answer[s]

            if not s:
                return True

            for word in wordDict:
                if s.startswith(word):
                    new_string = s[len(word) :]
                    if dp(new_string, wordDict, answer):
                        answer[s] = True
                        return True
            else:
                answer[s] = False
                return False

        return dp(s, wordDict)