def solution(m, n, puddles):
    dp = [[0] * n for _ in range(m)]
    if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            dp[a-1][b-1] = -1 

    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if dp[i][j] == -1:
                continue

            if i > 0 and dp[i - 1][j] != -1:
                dp[i][j] += dp[i - 1][j]

            if j > 0 and dp[i][j - 1] != -1:
                dp[i][j] += dp[i][j - 1]

            dp[i][j] %= 1000000007

    return dp[m - 1][n - 1]
