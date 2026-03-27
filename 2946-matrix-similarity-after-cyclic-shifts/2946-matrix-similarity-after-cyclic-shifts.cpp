#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool areSimilar(vector<vector<int>>& mat, int k) {
        auto grid = mat;

        for (int i = 0; i < k; i++) {
            for (auto& row : grid) {
                if (k % 2 == 0)
                    rotate(row.begin(), row.begin() + 1, row.end());
                else
                    rotate(row.begin(), row.end() - 1, row.end());
            }
        }

        return grid == mat;
    }
};