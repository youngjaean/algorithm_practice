class Solution {
public:
    bool checker(char c){
        return strchr("aeiou", c) != NULL;
    }

    bool doesAliceWin(string s) {
        for(auto c : s){
            if(checker(c)){
                return true;
            }
        }

        return false;
    }
};