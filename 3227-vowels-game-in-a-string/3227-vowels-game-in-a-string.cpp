class Solution {
public:
    bool checker(char c){
        return strchr("aeiou", c) != NULL;
    }

    bool doesAliceWin(string s) {
        int turn = 1;
        int vowels = 0;

        for(auto c : s){
            if(checker(c)){
                vowels += 1;
                break;
            }
        }

        return vowels == 1;
    }
};