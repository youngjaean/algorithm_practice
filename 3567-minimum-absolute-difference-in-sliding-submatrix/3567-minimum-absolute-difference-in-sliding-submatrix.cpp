#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    vector<vector<int>> minAbsDiff(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();

        vector<vector<int>> res(m - k + 1, vector<int>(n - k + 1));

        for(int i = 0; i + k <= m; i++){
            for(int j = 0; j + k <= n; j++){

                vector<int> submatrix;
                for(int x = i; x < i + k; x++){
                    for(int y = j; y < j + k; y++){
                        submatrix.push_back(grid[x][y]);
                    }
                }
                sort(submatrix.begin(), submatrix.end());
                int answer = INT_MAX;
                for(int t = 1; t < (int)submatrix.size(); t++){
                    if (submatrix[t] == submatrix[t-1])
                        continue;
                    answer = min(answer, abs(submatrix[t] - submatrix[t -1]));
                }
                if (answer != INT_MAX)
                    res[i][j] = answer;
            }
        }

        return res;
    }
};