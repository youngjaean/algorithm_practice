def solution(want, number, discount):
    answer = 0

    for i in range(len(discount)):
        new_discount = discount[i : i + 10]
        for i in range(len(want)):
            if new_discount.count(want[i]) != number[i]:
                getit = False

                break
            else:
                getit = True
        if getit:
            answer += 1

    return answer