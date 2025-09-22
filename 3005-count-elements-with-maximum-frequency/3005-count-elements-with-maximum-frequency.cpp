class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        // nums 중 최대값 찾기
        int maxVal = *max_element(nums.begin(), nums.end());
        
        // 최대값 크기의 vector 생성 (인덱스 0부터 maxVal까지 사용)
        vector<int> freq(maxVal + 1, 0);
        
        // nums의 각 요소에 해당하는 인덱스에 +1
        for (int num : nums) {
            freq[num]++;
        }
        
        // 큰 값 기준으로 정렬 (내림차순)
        sort(freq.begin(), freq.end(), greater<int>());
        
        // 가장 앞에 있는 값과 같은 값들의 합 계산
        int maxFreq = freq[0];
        int result = maxFreq;
        
        for (int i = 1; i < freq.size(); i++) {
            if (freq[i] == maxFreq) {
                result += freq[i];
            } else {
                break;
            }
        }
        
        return result;
    }
};