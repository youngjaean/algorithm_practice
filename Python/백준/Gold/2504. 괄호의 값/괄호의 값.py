def chcek_barcket(barcket_list):
    value = {"(": 2, "[": 3}
    barcket_dic = {")": "(", "]": "["}
    stack = []
    tmp, answer = 1, 0
    previous_bracket = ""
    if barcket_list[0] == ")" or barcket_list[0] == "]":
        return 0
    elif barcket_list[-1] == "(" or barcket_list[-1] == "[":
        return 0
    else:
        for barcket in barcket_list:
            if not barcket in barcket_dic:
                tmp *= value[barcket]
                stack.append(barcket)
            else:
                if not stack:
                    return 0
                else:
                    target = barcket_dic[barcket]
                    if target != stack.pop():
                        return 0
                    else:
                        if not previous_bracket in barcket_dic:
                            answer += tmp

                        tmp //= value[target]

            previous_bracket = barcket
        if stack:
            return 0
    return answer


barckets_list = str(input())


print(chcek_barcket(barckets_list))