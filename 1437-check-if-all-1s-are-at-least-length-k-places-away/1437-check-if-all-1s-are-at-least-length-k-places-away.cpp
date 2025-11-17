#include <vector>
using namespace std;

class Solution
{
public:
    bool kLengthApart(vector<int> &nums, int k)
    {
        int count = 0;
        bool start = false;

        for (auto num : nums)
        {
            if (num == 0)
                count++;
            else if (num == 1)
            {
                if (start && count < k)
                {
                    return false;
                }
                start = true;
                count = 0;
            }
        }
        return true;
    }
};

