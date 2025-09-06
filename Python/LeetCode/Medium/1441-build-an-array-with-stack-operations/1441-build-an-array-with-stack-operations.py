class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        answer = []
        for i in range(1, target[-1] + 1):
            answer.append("Push")
            if i not in target:
                answer.append("Pop")

        return answer
