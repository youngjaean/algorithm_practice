class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        long long suffix = 1, prefix=1;
        int n = grid.size(), m = grid[0].size();
        vector<vector<int>> answer(n, vector<int>(m));

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                answer[i][j] = suffix;
                suffix =suffix* grid[i][j]  % 12345;
            }
        }


        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                answer[i][j] = answer[i][j] * prefix % 12345;
                prefix = prefix* grid[i][j] % 12345;
            }
        }

        return answer;
    }
};