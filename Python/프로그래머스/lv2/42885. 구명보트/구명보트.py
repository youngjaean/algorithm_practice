from collections import deque


def solution(peoples, limit):
    answer = 0
    peoples.sort(reverse=True)
    peoples = deque(peoples)
    while peoples:
        if peoples[0] + peoples[-1] <= limit and len(peoples) > 1:
            answer += 1
            peoples.popleft()
            peoples.pop()
        else:
            answer += 1
            peoples.popleft()

    return answer