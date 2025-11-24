class Solution {
public:
    vector<bool> prefixesDivBy5(vector<int>& nums) {
        vector<bool> answer;
        int toal = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            toal = ((toal << 1) + nums[i]) % 5;
            answer.emplace_back(toal == 0);
        }
        return answer;
    }
};