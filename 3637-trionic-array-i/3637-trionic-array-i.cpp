class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        const int n = (int)nums.size();
        if (n < 4) return false; 
        int state = 0; 
        int p = -1, q = -1;

        for (int i = 1; i < n; ++i) {
            if (nums[i] == nums[i - 1]) return false; 

            if (state == 0) {
                if (nums[i] > nums[i - 1]) {
                } else {
                    p = i - 1;      
                    state = 1;
                }
            } else if (state == 1) {
                if (nums[i] < nums[i - 1]) {
                } else { 
                    q = i - 1;     
                    state = 2;
                }
            } else {
                if (nums[i] > nums[i - 1]) {
                } else {
                    return false; 
                }
            }
        }

        if (state != 2) return false;
        if (!(0 < p && p < q && q < n - 1)) return false;

        return true;
    }
};
