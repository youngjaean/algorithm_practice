class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        check_list = []
        base_line = set()
        count_dict = {}
        for i, c in enumerate(s):
            count_dict[c] = i

        for i, c in enumerate(s):
            if c not in base_line:
                while (
                    check_list
                    and c < check_list[-1]
                    and i < count_dict[check_list[-1]]  # 여기서 중요한건, 해당 알파벳의 마지막 Index임 그렇기에, 마지막 인덱스가 아닌 경우와 알파벳 비교가 필요함 사전 충족을 위해
                ):
                    base_line.discard(check_list.pop())
                check_list.append(c)
                base_line.add(c)

        return "".join(check_list)