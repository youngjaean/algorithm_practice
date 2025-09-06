def solution(n):
    answer = 0
    i = 1
    while i <= n:
        tmp_n = n
        for j in range(i, n + 1):
            if tmp_n - j > 0:
                tmp_n -= j
            elif tmp_n - j == 0:
                answer += 1
                break
            elif tmp_n - j < 0:
                break
        i += 1
    return answer