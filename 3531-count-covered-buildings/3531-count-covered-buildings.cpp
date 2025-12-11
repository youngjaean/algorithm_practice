#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {

public:

int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
    unordered_map<int, vector<int>> xMap;
    int answer = 0;

    for (vector<int> building : buildings)
    {
        xMap[building[0]].push_back(building[1]) ;
    }
    for (const auto x : xMap)
    {   
        if(x.second.size() >=3 )
        {
            answer += x.second.size() - 2;
        }
    }
    
    return answer;


}

};