class Solution {
public:
    int minScoreTriangulation(vector<int>& values) {
        int n = values.size();
        vector<vector<int>> memo(n, vector<int>(n, -1));
        
        function<int(int, int)> dfs = [&](int i, int j) -> int {
            if (j - i < 2) return 0;
            if (memo[i][j] != -1) return memo[i][j];
            
            int res = INT_MAX;
            for (int k = i + 1; k < j; k++) {
                res = min(res, values[i] * values[k] * values[j] 
                              + dfs(i, k) + dfs(k, j));
            }
            return memo[i][j] = res;
        };
        
        return dfs(0, n - 1);
    }
};