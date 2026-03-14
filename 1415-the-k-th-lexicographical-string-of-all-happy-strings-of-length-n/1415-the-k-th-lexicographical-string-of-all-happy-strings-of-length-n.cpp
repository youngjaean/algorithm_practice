class Solution {
public:
    vector<char> chars = {'a','b','c'};
    int count = 0;

    string dfs(string cur, int n, int k)
    {
        if (cur.size() == n){
            count++;
            if (count == k) return cur;
            return "";
        }

        for (char c : chars){
            if (!cur.empty() && cur.back() == c) continue;

            string res = dfs(cur + c, n, k);
            if (res != "") return res;
        }

        return "";
    }

    string getHappyString(int n, int k) {
        return dfs("", n, k);
    }
};