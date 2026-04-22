class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []

        for query in queries:
            for word in dictionary:
                count = 0

                for i in range(len(word)):
                    if query[i] != word[i]:
                        count += 1
                    if count > 2:
                        break

                if count <= 2:
                    ans.append(query)
                    break

        return ans