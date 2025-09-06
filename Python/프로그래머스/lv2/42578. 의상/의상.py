def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        try:
            clothes_dict[cloth[1]] += 1
        except:
            clothes_dict[cloth[1]] = 2

    for value in clothes_dict.values():
        answer *= value

    return answer - 1