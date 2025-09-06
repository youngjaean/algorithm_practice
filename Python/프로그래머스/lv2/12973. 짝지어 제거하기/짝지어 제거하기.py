def solution(s):
    tmp = []
    for a in s:
        if len(tmp) == 0:
            tmp.append(a)
        else:
            if tmp[-1] == a:
                tmp.pop()
            else:
                tmp.append(a)
    if len(tmp) == 0:
        return 1
    else:
        return 0