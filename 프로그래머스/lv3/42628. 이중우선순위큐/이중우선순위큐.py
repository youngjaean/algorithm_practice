def solution(operations):
    answer = []
    for oper in operations:
        if "I" in oper:
            answer.append(int(oper[2:]))
        elif "D 1" == oper and answer:
            answer.sort()
            answer.pop()
        elif "D -1" == oper and answer:
            answer.sort(reverse=True)
            answer.pop()
        else:
            pass
    if not answer:
        return [0, 0]
    else:
        return max(answer), min(answer)
