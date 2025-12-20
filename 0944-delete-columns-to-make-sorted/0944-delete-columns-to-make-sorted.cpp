#include <string>
#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    int minDeletionSize(vector<string>& strs) {
        unordered_map<int, string> check_map;
        
        for(const auto& str : strs)
        {
            for (int i = 0; i < str.size(); i++)
            {
                check_map[i] += str[i];
            }
        }
        
        int answer = 0;

        for (const auto& checking : check_map)
        {
            string sorted_str = checking.second;
            sort(sorted_str.begin(), sorted_str.end());
            if (checking.second != sorted_str)
                answer++;
        }

        return answer;
    }
};