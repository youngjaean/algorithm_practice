class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> ans;
        for (int h = 0; h < 12; ++h) {
            for (int m = 0; m < 60; ++m) {
                if (__builtin_popcount(h) + __builtin_popcount(m) == turnedOn) // 결국 시간과 분은 bit의 가중치로 접근해야했으며 
                //아주 작은 값이기에 완전 탐색 그리고 비트 개수를 측정하는게 답이였음.
                 {
                    ans.push_back(to_string(h) + ":" + (m < 10 ? "0" : "") +
                                  to_string(m));
                }
            }
        }
        return ans;
    }
};