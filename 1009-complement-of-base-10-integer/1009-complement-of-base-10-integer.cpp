class Solution {
public:
    int bitwiseComplement(int n) {
        if (n==0) return 1;
        string s;
        while(n>0){
            s += ((n % 2)? 0 : 1) + '0';
            n /= 2;
        }
        reverse(s.begin(), s.end());

        int x = stoi(s, nullptr, 2);

        return x;
    }
};
