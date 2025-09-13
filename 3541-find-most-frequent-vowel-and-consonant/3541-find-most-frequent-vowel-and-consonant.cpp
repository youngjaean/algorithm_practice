class Solution
{
public:
    int maxFreqSum(string s)
    {
        unordered_map<char, int> vowels;
        unordered_map<char, int> consonants;

        for (auto c : s)
        {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            {
                vowels[c] += 1;
            }
            else
            {
                consonants[c] += 1;
            }
        }
        int maxVowelFreq = 0;
        if (!vowels.empty())
        {
            maxVowelFreq = max_element(vowels.begin(), vowels.end(),
                                       [](const pair<char, int> &a, const pair<char, int> &b)
                                       { return a.second < b.second; })
                               ->second;
        }

        int maxConsonantFreq = 0;
        if (!consonants.empty())
        {
            maxConsonantFreq = max_element(consonants.begin(), consonants.end(),
                                           [](const pair<char, int> &a, const pair<char, int> &b)
                                           { return a.second < b.second; })
                                   ->second;
        }

        return maxVowelFreq + maxConsonantFreq;
    }
};