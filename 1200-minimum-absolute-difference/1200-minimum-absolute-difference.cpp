#include <algorithm>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        map<int, vector<vector<int>>> candidate;
        for (int i = 0; i < arr.size() - 1; i++ )
        {
            candidate[abs(arr[i] - arr[i+1])].push_back( {arr[i], arr[i+1]});
        }

        auto it = candidate.begin();
        return  it -> second;
        

    }
};