class Solution {
public:
    int smallestRepunitDivByK(int k) {
        int answer = 0;
        if (k == 1) return 1;

        if (k % 2 == 0 || k % 5 == 0) return -1;

        for(int i = 1; i<= k ; i++)
        {
            answer = (answer * 10 + 1) % k;
            if (answer  == 0) return i;
        }

        return -1;
    }
};