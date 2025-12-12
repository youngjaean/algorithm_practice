#include <vector>
#include <string>
#include <sstream>  
using namespace std;

class Solution {
public:
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        vector<vector<int>> mentions(numberOfUsers, vector<int>(2, 0));
        
		sort(events.begin(), events.end(), [](const vector<string>& a, const vector<string>& b)
		 {
		    if (stoi(a[1]) != stoi(b[1])) return stoi(a[1]) < stoi(b[1]);
			    return a[0] == "OFFLINE";  
		});
        for (const auto& event : events)  
        {
            if (event[0] == "OFFLINE")
            {
                int user_id = stoi(event[2]); 
                int new_offline_until = stoi(event[1]) + 60; 
                mentions[user_id][1] = max(mentions[user_id][1], new_offline_until);  
            }
            else
            {
                if (event[2] == "ALL")
                {
                    for (auto& mention : mentions) 
                    {
                        mention[0]++;
                    }
                }
                else if (event[2] == "HERE")
                {		
                    for (auto& mention : mentions)
                    {
                        if (mention[1] <= stoi(event[1]))
                        {
                            mention[0]++;
                            mention[1] = 0;
                        }
                    }
                } 
                else
                { 
                    stringstream ss(event[2]);
                    string token;
                    while (ss >> token) 
                    { 
                        mentions[stoi(token.substr(2))][0]++;
                    }
                }
            }
        }
        
        vector<int> result;
        for (const auto& mention : mentions) {
            result.push_back(mention[0]);
        }
        return result;  
    }
};  