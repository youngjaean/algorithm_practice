class Solution
{
public:
    long long fn(int num)
    {
        if (num <= 3)
            return num;
        int cnt = 2;
        int pre = 3;

        long long ans = 3;

        for (int i = 4; i <= num; i*=4)
        {
            long long upper = 1LL * i * 4 - 1;
            long long range = 0;

            if (upper >= num)
            {
                range = num - pre;
            }
            else
                range = upper - pre;

            pre = upper;

            ans += (1LL * range * cnt);
            cnt++;
        }

        return ans;
    }

    long long minOperations(vector<vector<int>> &queries)
    {
        long long ans = 0;

        for (auto q : queries)
        {
            int lv = q[0], rv = q[1];

            long long max_num = fn(rv);
            long long min_num = fn(lv - 1);

            long long diff = max_num - min_num;

            if (diff % 2)
                diff++;

            ans += (diff / 2);
        }

        return ans;
    }
};