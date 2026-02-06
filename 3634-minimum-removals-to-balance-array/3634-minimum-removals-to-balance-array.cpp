#include <algorithm>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (n <= 1) return 0;

        sort(nums.begin(), nums.end());

        int ans = INT_MAX;
        int j = 0;

        for (int i = 0; i < n; ++i) {
            if (j < i) j = i;

            long long pivot = 1LL * nums[i] * k;
            while (j + 1 < n && nums[j + 1] <= pivot) ++j;

            int removeValue = i + (n - 1 - j);
            ans = min(ans, removeValue);
        }

        return ans;
    }
};
