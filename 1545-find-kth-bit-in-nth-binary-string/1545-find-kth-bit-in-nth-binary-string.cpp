#include <string>
using namespace std;

class Solution {
public:
    char findKthBit(int n, int k) {
        string pre_string = " 0";
        string cruent_string = " 0";

        int i = 1;

        while (i < n) {
            cruent_string += "1";

            for (int j = pre_string.size() - 1; j >= 1; j--) {
                if (pre_string[j] == '0') {
                    cruent_string += '1';
                } else {
                    cruent_string += '0';
                }
            }

            pre_string = cruent_string;
            i++;
        }

        return cruent_string[k];
    }
};