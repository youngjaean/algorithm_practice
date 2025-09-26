#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int answer = 0;
        for (int i = 0; i < nums.size() -1; i++)
        {
            for(int j = i+1; j < nums.size(); j++){
                int summer = nums[i] + nums[j];
                answer+= lower_bound(nums.begin() + j + 1, nums.end(), summer) - (nums.begin() + j + 1) ;
            }

        }

        return answer;
    };
};