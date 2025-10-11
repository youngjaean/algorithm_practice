#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution
{
public:
    long long maximumTotalDamage(vector<int> &power)
    {
        sort(power.begin(), power.end());
        vector<long long> tablula(power.size(), 0);
        unordered_map<int, int> count_table;
        tablula[0] = power[0];
        count_table[power[0]] += 1;

        for (int i = 1; i < power.size(); i++)
        {
            if (power[i - 1] == power[i])
            {
                tablula[i] = tablula[i - 1] + power[i];
                count_table[power[i]] += 1;
            }
            else if (power[i - 1] < power[i] - 2)
            {
                tablula[i] = max(tablula[i - 1] + (long long)power[i], (long long)power[i]);
                count_table[power[i]] += 1;
            }
            else
            {
                int skip_count = 0;
                for (int val = power[i] - 2; val <= power[i]; val++)
                {
                    skip_count += count_table[val];
                }

                long long max_val = 0;
                for (int j = 0; j < 3 && i - skip_count - j >= 0; j++)
                {
                    int idx = i - skip_count - j;
                    if (idx >= 0 && idx < power.size())
                    {
                        int condidate_value = power[idx];
                        if (condidate_value < power[i] - 2)
                        {
                            max_val = max(tablula[idx] + power[i], tablula[i - 1]);
                            break;
                        }
                    }
                }
                tablula[i] = max(max_val, (long long)power[i]);
                count_table[power[i]] += 1;
            }
        }

        return tablula.back();
    }
};