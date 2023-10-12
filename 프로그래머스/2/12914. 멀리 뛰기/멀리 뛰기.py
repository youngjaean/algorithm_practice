def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    # if n > 4 and n % 2 == 0:
    #     return (dp[n] - 1) %1234567
    # else:
    return (dp[n]) %1234567