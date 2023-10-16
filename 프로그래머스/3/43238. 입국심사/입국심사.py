def check_(n, times, current):
    return n <= sum(current // i for i in times)


def solution(n, times):
    a, b = 0, 1
    while not check_(n, times, b):
        a, b = b, b * 2
    while a < b:
        m = (a + b) // 2
        a, b = (a, m) if check_(n, times, m) else (m + 1, b)
    return a
