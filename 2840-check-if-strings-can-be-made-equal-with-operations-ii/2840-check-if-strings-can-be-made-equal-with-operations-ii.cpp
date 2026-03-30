#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    bool checkStrings(string s1, string s2) {
        string evenS1 = "";
        string evenS2 = "";
        string oddS1 = "";
        string oddS2 = "";

        for (int i = 0; i < s1.size(); i++) {
            if (i % 2 == 0) {
                evenS1.push_back(s1[i]);
                evenS2.push_back(s2[i]);
            } else {
                oddS1.push_back(s1[i]);
                oddS2.push_back(s2[i]);
            }
        }

        sort(evenS1.begin(), evenS1.end());
        sort(evenS2.begin(), evenS2.end());
        sort(oddS1.begin(), oddS1.end());
        sort(oddS2.begin(), oddS2.end());

        return evenS1 == evenS2 && oddS1 == oddS2;
    }
};