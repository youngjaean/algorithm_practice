def solution(s):
    num = list(map(int, s.split(" ")))
    min_value = min(num)
    max_value = max(num)
    answer = str(min_value) + " " + str(max_value)
    return answer