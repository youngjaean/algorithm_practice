
class Solution
{
public:
    int maxFreqSum(string s)
    {
        unordered_map<char, int> string_map;
        int count_vowels = 0;
        int count_consonants = 0;

        for (auto c : s)
        {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            {
                string_map[c] += 1;
                count_vowels = max(count_vowels, string_map[c]);
            }
            else
            {
                string_map[c] += 1;
                count_consonants = max(count_consonants, string_map[c]);
            }
        }

        return count_vowels + count_consonants;
    }
};