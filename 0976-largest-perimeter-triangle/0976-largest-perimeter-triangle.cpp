#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int largestPerimeter(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());

        int index = nums.size() - 1;
        while (index >= 2)
        {
            int tmp = nums[index - 2] + nums[index - 1];
            if (tmp > nums[index])
            {
                return tmp + nums[index];
            }
            else
            {
                index -= 1;
            }
        }
        return 0;
    }
};