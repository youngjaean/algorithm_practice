class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        sort(nums.begin(), nums.end());
        
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        int maxFreq = 0;
        set<long long> candidates;  
        
        for (int num : nums) {
            candidates.insert(num);
            candidates.insert((long long)num - k);
            candidates.insert((long long)num + k);
        }
        
        for (long long target : candidates) {
            long long rangeMin = target - k;
            long long rangeMax = target + k;
            
            auto left = lower_bound(nums.begin(), nums.end(), rangeMin);
            auto right = upper_bound(nums.begin(), nums.end(), rangeMax);
            int inRange = right - left;
            
            int alreadyTarget = 0;
            if (target >= INT_MIN && target <= INT_MAX) {
                alreadyTarget = freq[(int)target];
            }
            
            int needOperation = inRange - alreadyTarget;
            int totalFreq = alreadyTarget + min(numOperations, needOperation);
            
            maxFreq = max(maxFreq, totalFreq);
        }
        
        return maxFreq;
    }
};