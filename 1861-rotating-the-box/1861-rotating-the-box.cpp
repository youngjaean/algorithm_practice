class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        int n = boxGrid.size();
        int m = boxGrid[0].size();

        vector<vector<char>> res(m, vector<char>(n, '.'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                res[j][n - 1 - i] = boxGrid[i][j];
            }
        }

        for (int col = 0; col < n; col++) {

            int emptyRow = m - 1;

            for (int row = m - 1; row >= 0; row--) {

                if (res[row][col] == '*') {
                    emptyRow = row - 1;
                }
                else if (res[row][col] == '#') {

                    swap(res[row][col], res[emptyRow][col]);
                    emptyRow--;
                }
            }
        }

        return res;
    }
};