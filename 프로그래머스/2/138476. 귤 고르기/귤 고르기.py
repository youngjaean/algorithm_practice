from collections import defaultdict


def solution(k, tangerine):
    tangerine_dcit = defaultdict(int)
    for tan in tangerine:
        tangerine_dcit[tan] += 1
    answer = 0
    numbuer = 0
    tangerine_dcit = sorted(tangerine_dcit.items(), key=lambda k: k[1], reverse=True)

    for _, value in tangerine_dcit:
        if numbuer < k:
            numbuer += value
            answer += 1
        else:
            break
    return answer
