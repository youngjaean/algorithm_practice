#include <vector>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    vector<int> findXSum(vector<int> &nums, int k, int x)
    {
        vector<int> answer;

        for (int i = 0; i <= nums.size() - k; i++)
        {
            unordered_map<int, int> frequency;
            for (int j = 0; j < k; j++)
                frequency[nums[i + j]]++;
            std::vector<std::pair<int, int>> sorted(frequency.begin(), frequency.end());

            sort(sorted.begin(), sorted.end(),
                 [](const auto &a, const auto &b)
                 {
                     if (a.second != b.second)
                         return a.second > b.second;
                     return a.first > b.first;
                 });
            int sum = 0;
            for (int y = 0; y < x && y < sorted.size(); y++)
                sum += sorted[y].first * sorted[y].second;
            answer.push_back(sum);
        }

        return answer;
    }
};