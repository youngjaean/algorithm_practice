class Solution {
public:
    int minPairSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end()); // 오름차순

        int n = nums.size();
        int ans = 0;

        for (int i = 0; i < n / 2; ++i) {
            ans = std::max(ans, nums[i] + nums[n - 1 - i]);
        }

        return ans;
    }
};
