class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        check = {"]": "[", ")": "(", "}": "{"}
        stack = []

        for c in s:
            if c not in check:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if check[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False

        if not len(stack):
            return True

        else:
            return False

