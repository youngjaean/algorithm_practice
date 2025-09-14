#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <cctype> 

using namespace std;

class Solution
{
public:
    string toLowerCase(string s)
    {
        for (char &c : s)
        {
            c = tolower(c);
        }
        return s;
    }

    bool isVowel(char c)
    {
        c = tolower(c);
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    string vowelPattern(string s)
    {
        s = toLowerCase(s);
        for (char &c : s)
        {
            if (isVowel(c))
            {
                c = '*';
            }
        }
        return s;
    }

    vector<string> spellchecker(vector<string> &wordlist, vector<string> &queries)
    {
        unordered_set<string> exactWords;
        unordered_map<string, string> lowerMap;
        unordered_map<string, string> vowelMap;

        // wordlist 전처리
        for (const string &word : wordlist)
        {
            exactWords.insert(word);

            string lower = toLowerCase(word);
            if (lowerMap.find(lower) == lowerMap.end())
            {
                lowerMap[lower] = word;
            }

            string pattern = vowelPattern(word);
            if (vowelMap.find(pattern) == vowelMap.end())
            {
                vowelMap[pattern] = word;
            }
        }

        vector<string> result;
        for (const string &query : queries)
        {
            if (exactWords.count(query))
            {
                result.push_back(query);
            }
            else if (lowerMap.count(toLowerCase(query)))
            {
                result.push_back(lowerMap[toLowerCase(query)]);
            }
            else if (vowelMap.count(vowelPattern(query)))
            {
                result.push_back(vowelMap[vowelPattern(query)]);
            }
            else
            {
                result.push_back("");
            }
        }

        return result;
    }
};