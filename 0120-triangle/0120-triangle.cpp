#include <vector>

using namespace std;

class Solution
{
public:
    int minimumTotal(vector<vector<int>> &triangle)
    {
        vector<int> tabulation = triangle[triangle.size() - 1];
        for (int i = triangle.size() - 2; i >= 0; --i) 
        {
            for (int j = 0; j < triangle[i].size(); ++j)  
            {
                tabulation[j] = triangle[i][j] + min(tabulation[j], tabulation[j + 1]);
            }
        }
        
        return tabulation[0];
    }
};