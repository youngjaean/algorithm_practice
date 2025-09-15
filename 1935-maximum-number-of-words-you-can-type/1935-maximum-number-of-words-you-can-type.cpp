#include <string>
#include <sstream>
#include <vector>
#include <algorithm> 

using namespace std;
class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        stringstream ss(text);
        string word;
        int count = 0;

        while (ss >> word)

        {
            bool hasBrokenLetter = any_of(brokenLetters.begin(), brokenLetters.end(),
                                [&word](char c) {return word.find(c) != string::npos;});

            if (!hasBrokenLetter)
                count ++;
        }

        return count++;
    }
};