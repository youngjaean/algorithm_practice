class Bank {
public:
    vector<long long>& balance;
    int length;
    Bank(vector<long long>& balance) : balance(balance) {
        length = balance.size();
    }
    
    bool checkRange(int account){
        return account < 1 || account > length;
    }
    
    bool transfer(int account1, int account2, long long money) {
        if (checkRange(account1) || checkRange(account2) || balance[account1 - 1] < money)
             return false;
        balance[account1 - 1] -= money;
        balance[account2 - 1] += money;
        return true;
    }
    
    bool deposit(int account, long long money) {
        if (checkRange(account))
            return false;
        balance[account - 1] += money;
        return true;
        
    }
    
    bool withdraw(int account, long long money) {
        if (checkRange(account) || balance[account - 1] < money)
            return false;
        
        balance[account - 1] -= money;
        return true;
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */