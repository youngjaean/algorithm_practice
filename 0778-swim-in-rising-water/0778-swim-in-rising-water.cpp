class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        int dx[] = {0, 1, 0, -1};
        int dy[] = {1, 0, -1, 0};
        
        pq.push({grid[0][0], 0, 0});
        
        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            
            int cost = curr[0], x = curr[1], y = curr[2];
            
            if (visited[x][y]) continue;
            visited[x][y] = true;
            
            if (x == n - 1 && y == n - 1) return cost;
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny]) {
                    pq.push({max(cost, grid[nx][ny]), nx, ny});
                }
            }
        }
        return -1;
    }
};