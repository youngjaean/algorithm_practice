
class Solution
{
public:
    int totalMoney(int n)
    {

        int total = 0;
        int start = 0;

        for (int i = 0; i < n; i++)
        {
            if (i % 7 == 0)
                start += 1;
            total += (i % 7 + start);
        }

        return total;
    }
};
