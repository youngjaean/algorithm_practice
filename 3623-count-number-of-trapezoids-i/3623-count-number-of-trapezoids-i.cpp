#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;


class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        long long ans = 0, sum = 0;
        const int mod = 1e9 + 7;
        unordered_map<int, int> top_map;
        for (auto point: points){
     
        top_map[point[1]] += 1;
        }
        for (auto it: top_map){

            long long tmp = (long long)it.second * (it.second - 1) / 2;

            ans += tmp * sum;
            sum += tmp;
        }
        return ans % mod;    
        
    }
};