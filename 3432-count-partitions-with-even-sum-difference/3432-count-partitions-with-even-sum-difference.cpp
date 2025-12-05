class Solution {
public:
    int countPartitions(vector<int>& nums) {
        int right = 0, ans = 0;
        int left = std::accumulate(nums.begin(), nums.end(), 0);
        for (int i = 0; i < nums.size() - 1; ++i) {
            right += nums[i];
            left -= nums[i];
            if ((right - left) % 2 == 0)
                ans++;
        }
        return ans;
    }
};