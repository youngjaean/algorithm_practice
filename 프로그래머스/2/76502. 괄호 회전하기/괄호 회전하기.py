def check_(s):
    start_clip = ["(", "[", "{"]
    check_dict = dict({")": "(", "}": "{", "]": "["})
    check_list = []
    for c in s:
        if c in start_clip:
            check_list.append(c)
        elif not check_list or check_dict[c] != check_list[-1]:
            return False
        elif check_dict[c] in check_list:
            check_list.pop(-1)

    if not check_list:
        return True
    else:
        return False


def solution(s):
    answer = 0
    if len(s) % 2 != 0:
        return 0
    if check_(s):
        answer += 1
    for i in range(len(s) - 1):
        s = s[1:] + s[0]
        if check_(s):
            answer += 1
    return answer
