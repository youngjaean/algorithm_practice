#include <vector>
#include <set>
#include <queue>
#include <unordered_map>
using namespace std;

class Router
{
    set<vector<int>> mpp;
    queue<vector<int>> router;
    unordered_map<int, vector<int>> timestamps;
    unordered_map<int, int> st;
    int maxSize = 0;

public:
    Router(int memoryLimit) : maxSize(memoryLimit)
    {
    }

    bool addPacket(int source, int destination, int timestamp)
    {
        vector<int> packet = {source,
                              destination,
                              timestamp};
        if (mpp.count(packet))
            return false;
        if (router.size() == maxSize)
        {
            vector<int> res = router.front();
            mpp.erase(res);
            int temp = res[1];
            st[temp]++;
            router.pop();
        }

        router.push(packet);
        mpp.insert(packet);
        timestamps[destination].push_back(timestamp);
        return true;
    }

    vector<int> forwardPacket()
    {
        if (router.empty())
            return {};
        vector<int> res = router.front();
        router.pop();
        mpp.erase(res);
        int temp = res[1];
        st[temp]++;
        return res;
    }

    int getCount(int destination, int startTime, int endTime)
    {
        if (timestamps.find(destination) == timestamps.end())
            return 0;
        auto &p = timestamps[destination];
        int temp = st[destination];
        auto right = lower_bound(p.begin() + temp, p.end(), startTime);
        auto left = upper_bound(p.begin() + temp, p.end(), endTime);
        return int(left - right);
    }
};