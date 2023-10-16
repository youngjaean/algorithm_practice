def solution(elements: list):
    answer = []
    length = len(elements)
    elements *= 2
    for i in range(length):
        for j in range(1, length + 1):
            answer.append(sum(elements[i : i + j]))

    return len(set(answer))
