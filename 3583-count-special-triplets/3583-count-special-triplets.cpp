#include <vector>
using namespace std;

class Solution {

public:

int specialTriplets(vector<int>& nums) {
    int answer = 0;
    bool half = false;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        if (nums[i] % 2 != 0)
        {
            continue;
        }
        for (int j = i + 1; j< n; j++)
        {
            if(2*nums[j]  == nums[i])
            {
                half = true;
            }
            if(half && nums[i] == nums[j])
            {
                answer++;
                break;
            }
        }
    }
    return answer;
}

};

