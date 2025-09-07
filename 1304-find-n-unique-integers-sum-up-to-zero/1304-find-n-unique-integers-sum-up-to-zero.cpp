class Solution
{
public:
    vector<int> sumZero(int n)
    {
        vector<int> output;
        if (n == 1)
            return {0};
        switch (n % 2)
        {
        case 0:
            for (int i = 1; i <= n / 2; i++)
            {
                output.push_back(-i);
                output.push_back(i);
            }
            break;
        case 1:
            for (int i = 1; i <= n / 2; i++)
            {
                output.push_back(-i);
                output.push_back(i);
            }
            output.push_back(0);
            break;
        }
        return output;
    }
};