def solution(priorities, location):
    max_value = max(priorities)
    answer_value = priorities[location]
    cand_list = []
    for i, value in enumerate(priorities):
        cand_list.append([i, value])
    answer = 0
    while cand_list:
        candidat_value = cand_list.pop(0)
        if candidat_value[1] >= max_value:
            answer += 1
            if candidat_value[1] == answer_value and candidat_value[0] == location:
                return answer
            max_value = max(cand_list, key=lambda x: x[1])[1]

        else:
            cand_list.append(candidat_value)