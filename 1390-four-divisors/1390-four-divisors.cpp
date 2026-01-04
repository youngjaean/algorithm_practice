#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int answer = 0;

        for (int num : nums) {
            vector<int> divisor;
            int limit = sqrt(num);

            for (int i = 1; i <= limit; i++) {
                if (num % i == 0) {
                    divisor.push_back(i);
                    if (i != num / i) {
                        divisor.push_back(num / i);
                    }
                }
            }

            if (divisor.size() == 4) {
                answer += divisor[0] + divisor[1] + divisor[2] + divisor[3];
            }
        }
        return answer;
    }
};
