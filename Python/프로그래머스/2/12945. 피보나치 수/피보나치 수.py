def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        dp = [0] + [0] * n
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i -  1]

        return dp[n]% 1234567
