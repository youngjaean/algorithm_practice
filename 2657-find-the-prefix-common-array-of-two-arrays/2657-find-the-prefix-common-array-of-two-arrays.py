class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        c = []
        for i in range(n):
            new_a = set(A[:i+1])
            new_b = set(B[:i+1])

            answer = len(new_a & new_b)
            c.append(answer)


        return c

             

