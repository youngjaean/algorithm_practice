#include <vector>

using namespace std;

class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        vector<long long> dp(n + 1, 0);
        dp[1] = 1;
        long long share = 0, MOD = 1000000007;
        for (int t = 2; t < n + 1; t++)
        {
            if (t - delay > 0) 
            {
                share = (share + dp[t - delay] + MOD) % MOD;  // MODE -> MOD
            }
            if (t - forget > 0)
            {
                share = (share - dp[t - forget] + MOD) % MOD;  // 세미콜론 중복 제거
            }

            dp[t] = share;
        }

        long long know = 0;

        for (int i = n - forget + 1; i <= n; i++)  // i ,= n -> i <= n
            know = (know + dp[i]) % MOD;
            
        return (int)know;
    }
};