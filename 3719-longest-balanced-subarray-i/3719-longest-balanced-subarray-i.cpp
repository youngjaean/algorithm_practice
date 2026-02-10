#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        // unique set
        unordered_set<int> unique_nums(nums.begin(), nums.end());

        int odd = 0;
        int even = 0;

        for (int num : unique_nums)
        {
            if (num % 2 == 0)
                even++;
            else
                odd++;
        }

        unordered_map<int, int> freq;
        for (int num : nums)
        {
            freq[num]++;
        }

        int max_duplicate = 0;
        for (const auto& [value, count] : freq)
        {
            if (count > 1)
                max_duplicate = max(max_duplicate, count - 1);
        }
        if (even != 0 && odd != 0 )
            return min(even, odd) * 2 + max_duplicate;
        else return 0;
    }
};
