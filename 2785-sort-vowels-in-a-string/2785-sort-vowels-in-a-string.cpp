using namespace std; 
class Solution {
public:
    bool check(char c){
        return strchr("aeiouAEIOU", c) != NULL;
    }

    string sortVowels(string s) {
        string temp ;
        for (auto c : s)
        {
           if (check(c)) {
            temp += c;
           }
        }
         sort(temp.begin(), temp.end());

        int j = 0;
        string ans;
        for (int i = 0; i <s.size(); i++)
        {
            if (check(s[i]))
            {
                ans += temp[j];
                j++;
            }else{
                ans += s[i];
            }
        }
    
        return ans;
    }
};