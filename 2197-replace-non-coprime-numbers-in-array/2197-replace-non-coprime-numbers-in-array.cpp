#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:

  vector<int> replaceNonCoprimes(vector<int>& nums) {
    vector<int> result;
    
    for (int i = 0; i < nums.size(); i++) {
        result.push_back(nums[i]);
        while (result.size() >= 2) {
            int n = result.size();
            if (gcd(result[n-2], result[n-1]) > 1) {
                int merged = lcm(result[n-2], result[n-1]);
                result.pop_back();
                result.pop_back();
                result.push_back(merged);
            } else {
                break;
            }
        }
    }
    
    return result;
}
};