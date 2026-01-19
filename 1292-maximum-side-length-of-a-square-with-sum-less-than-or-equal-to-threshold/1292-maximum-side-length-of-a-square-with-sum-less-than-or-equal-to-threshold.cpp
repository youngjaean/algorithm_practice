#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int R = (int)mat.size();
        int C = (int)mat[0].size();
        int size_n = min(R, C);

        vector<vector<long long>> prefix(R + 1, vector<long long>(C + 1, 0));
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                prefix[i + 1][j + 1] = prefix[i + 1][j] + prefix[i][j + 1]
                                     - prefix[i][j] + mat[i][j];
            }
        }

        auto SUMGRIND = [&](int start_i, int end_i, int start_j, int end_j) -> long long {
            return prefix[end_i][end_j]
                 - prefix[start_i][end_j]
                 - prefix[end_i][start_j]
                 + prefix[start_i][start_j];
        };

        for (int len = size_n; len >= 1; --len) {
            for (int i = 0; i + len <= R; ++i) {
                for (int j = 0; j + len <= C; ++j) {
                    if (SUMGRIND(i, i + len, j, j + len) <= (long long)threshold) {
                        return len;
                    }
                }
            }
        }

        return 0;
    }
};
