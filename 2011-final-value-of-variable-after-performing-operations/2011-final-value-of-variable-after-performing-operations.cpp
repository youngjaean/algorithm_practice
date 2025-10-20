#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
    int finalValueAfterOperations(vector<string> &operations)
    {
        int x = 0;
        for (auto operation : operations)
        {
            if (operation[0] == '+' || operation[2] == '+')
                x++;
            else if (operation[0] == '-' || operation[2] == '-')
                x--;
        }

        return x;
    }
};