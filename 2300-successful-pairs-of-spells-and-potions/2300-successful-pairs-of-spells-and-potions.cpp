#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> successfulPairs(vector<int> &spells, vector<int> &potions, long long success)
    {
        sort(potions.begin(), potions.end());
        int sl = spells.size();
        int pl = potions.size();
        vector<int> ans(sl, 0);
        for (int i = 0; i < sl; i++)
        {
            int spell = spells[i];
            int left = 0;
            int right = pl - 1;

            while (left <= right)
            {
                int mid = left + (right - left) / 2;
                long long product = (long long)spell * (long long)potions[mid];
                if (product >= success)
                {
                    right = mid - 1;
                }
                else
                {
                    left = mid + 1;
                }
            }
            ans[i] = pl - left;
        }

        return ans;
    }
};