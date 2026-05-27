class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        state = dict()

        for ch in word:
            lower = ch.lower()

            if lower not in state:
                if ch.islower():
                    state[lower] = 1
                else:
                    state[lower] = -1

            else:
                if state[lower] == -1:
                    continue

                if ch.isupper():
                    if state[lower] == 1:
                        state[lower] = 2

                else:
                    if state[lower] == 2:
                        state[lower] = -1

        return sum(v == 2 for v in state.values())