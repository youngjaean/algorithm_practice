class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row_arry = [""] * numRows
        row_idx = 1
        upper = True
        for c in s:
            row_arry[row_idx - 1] += c
            if row_idx == numRows:
                upper = False
            elif row_idx == 1:
                upper = True

            if upper:
                row_idx += 1
            else:
                row_idx -= 1

        return "".join(row_arry)
