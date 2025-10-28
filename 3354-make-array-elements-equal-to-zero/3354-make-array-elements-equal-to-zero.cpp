class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        int len = nums.size(), output = 0, left = 0, right = 0;
        for (int num : nums) 
            right += num;
        for (int i = 0; i < nums.size(); i++)
        {
            left += nums[i];
            right -= nums[i];
            if (nums[i] == 0)
            {
                 if (left == right) 
                    output += 2;
                if (abs(left - right) == 1) 
                    output++;
            }
        }
        return output;
        
    }
};