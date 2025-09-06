from collections import Counter


def solution(k, tangerine):


    tangerine_num = Counter(tangerine)
    answer = 0
    num = 0
    for value in sorted(tangerine_num.values(), reverse=True):
        if num < k:
            num += value
            answer += 1
        else:
            break
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
