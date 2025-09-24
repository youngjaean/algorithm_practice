#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    string fractionToDecimal(int numerator, int denominator)
    {
        if (numerator == 0)
            return "0";
        
        string result;
        
        if ((numerator < 0) ^ (denominator < 0))
        {
            result += "-";
        }
        
        long long num = abs(static_cast<long long>(numerator));
        long long den = abs(static_cast<long long>(denominator));
        
        result += to_string(num / den);
        num %= den;
        
        if (num == 0)
            return result;
        
        result += ".";
        
        unordered_map<long long, int> remainderMap;
        while (num != 0)
        {
            if (remainderMap.find(num) != remainderMap.end())
            {
                int index = remainderMap[num];
                result.insert(index, "(");
                result += ")";
                break;
            }
            
            remainderMap[num] = result.length();
            
            num *= 10;
            result += to_string(num / den);
            num %= den;
        }
        
        return result;
    }
};