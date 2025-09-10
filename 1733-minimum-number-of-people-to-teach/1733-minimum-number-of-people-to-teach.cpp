#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool hasCommon(const vector<int>& v1, const vector<int>& v2){  // v2 타입 수정
        if (v1.size() < v2.size())
        {
            unordered_set<int> s1(v1.begin(), v1.end());
            for (int num : v2){
                if (s1.count(num)) return true;
            }
        }
        else
        {
            unordered_set<int> s2(v2.begin(), v2.end());
            for (int num : v1) {
                if (s2.count(num)) return true;
            }
        }

        return false;  
    }

    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {

        vector<int> v(n + 1, 0);
        for (auto friends : friendships)
        {
            if (!hasCommon(languages[friends[0]-1], languages[friends[1]-1]))  
            {
                for (auto ln: languages[friends[0]-1]) 
                    v[ln] += 1; 
                for (auto ln: languages[friends[1]-1])  
                    v[ln] += 1;  
            }
        }
        
        int minVal = *min_element(v.begin(), v.end()); 
        return n - minVal - 1;  
    }
};