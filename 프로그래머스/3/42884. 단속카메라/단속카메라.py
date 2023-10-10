def solution(routes: list):
    routes.sort()

    answer = 1
    cam = 3000

    for start, end in routes:
        if start > cam:
            answer += 1
            cam = end
        cam = min(cam, end)

    return answer