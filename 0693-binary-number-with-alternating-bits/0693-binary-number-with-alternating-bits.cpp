
class Solution {
public:
    bool hasAlternatingBits(int n) {
        char previous = char('0' + (n & 1));
        n >>= 1;

        while (n > 0) {
            char tmp = char('0' + (n & 1));
            if (tmp == previous) return false;
            previous = tmp;
            n >>= 1;
        }
        return true;
    }

};

