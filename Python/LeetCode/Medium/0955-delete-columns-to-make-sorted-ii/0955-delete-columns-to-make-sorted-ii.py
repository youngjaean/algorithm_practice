class Solution:
    def minDeletionSize(self, strs):
        tpse, list_length, n = zip(*strs), len(strs), len(strs[0])
        empty = [""] * list_length

        for nxt in tpse:
            temp = [empty[i] + nxt[i] for i in range(list_length)]
            if temp == sorted(temp):
                empty = temp

        return n - len(empty[0])