class Solution {
public:
    long long minTime(vector<int>& skill, vector<int>& mana) {
        int n = skill.size();
        int m = mana.size();
        
        vector<long long> f(n, 0);
        
        for (int j = 0; j < m; j++) {
            long long x = mana[j];
            long long now = f[0];  

            for (int i = 1; i < n; i++) {
                now = max(now + (long long)skill[i-1] * x, f[i]);
            }
            f[n-1] = now + (long long)skill[n-1] * x;
            
            for (int i = n-2; i >= 0; i--) {
                f[i] = f[i+1] - (long long)skill[i+1] * x;
            }
        }
        
        return f[n-1];
    }
};