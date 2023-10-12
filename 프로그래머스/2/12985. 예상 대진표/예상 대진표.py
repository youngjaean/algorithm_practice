def solution(n, a, b):
    answer = 1
    min_value = min(a, b)
    max_value = max(a, b)
    while not (
        min_value % 2 == 1 and max_value % 2 == 0 and max_value - min_value == 1
    ):
        answer += 1
        min_value = min_value // 2 + min_value % 2
        max_value = max_value // 2 + max_value % 2
    return answer