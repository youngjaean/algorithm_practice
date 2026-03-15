class Fancy {
public:
    static const long long MOD = 1000000007;
    vector<long long> nums;
    long long mul = 1;
    long long add = 0;

    long long modPow(long long a, long long e) {
        long long result = 1;
        a %= MOD;

        while (e > 0) {
            if (e & 1) {
                result = (result * a) % MOD;
            }
            a = (a * a) % MOD;
            e >>= 1;
        }
        return result;
    }

    long long modInv(long long x) {
        return modPow(x, MOD - 2);
    }

    Fancy() {
    }
    
    void append(int val) {
        long long normalized = ( (val - add + MOD) % MOD * modInv(mul) ) % MOD;
        nums.push_back(normalized);
    }
    
    void addAll(int inc) {
        add = (add + inc) % MOD;
    }
    
    void multAll(int m) {
        mul = (mul * m) % MOD;
        add = (add * m) % MOD;
    }
    
    int getIndex(int idx) {
        if (idx < 0 || idx >= (int)nums.size()) {
            return -1;
        }
        return (nums[idx] * mul + add) % MOD;
    }
};