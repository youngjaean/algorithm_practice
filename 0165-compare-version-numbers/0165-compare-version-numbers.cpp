#include <string>
#include <vector>
#include <sstream>

using namespace std;

class Solution
{
public:
    int compareVersion(string version1, string version2)
    {
        auto parseRevisions = [](string version) -> vector<int>
        {
            vector<int> revisions;
            stringstream ss(version);
            string token;
            
            while (getline(ss, token, '.')) {
                revisions.push_back(stoi(token));
            }
            
            return revisions;
        };
        
        vector<int> rev1 = parseRevisions(version1);
        vector<int> rev2 = parseRevisions(version2);
        
        int maxLen = max(rev1.size(), rev2.size());
        
        for (int i = 0; i < maxLen; i++) {
            int val1 = (i < rev1.size()) ? rev1[i] : 0;
            int val2 = (i < rev2.size()) ? rev2[i] : 0;
            
            if (val1 < val2) return -1;
            if (val1 > val2) return 1;
        }
        
        return 0;
    }
};