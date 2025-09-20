#include <vector>
#include <map>
#include <unordered_set>
using namespace std;

class Router
{
public:
    int memoryLimit = 0;
    int checkLimit = 0;
    bool isLimit = false;
    vector<vector<int>> router;
    map<int, vector<int>> destinaitonCheck;
    unordered_set<string> packetSet;

    string makeKey(int source, int destination, int timestamp)
    {
        return to_string(source) + "_" + to_string(destination) + "_" + to_string(timestamp);
    }

    Router(int memoryLimit)
    {
        this->memoryLimit = memoryLimit;
    }

    bool addPacket(int source, int destination, int timestamp)
    {
        string key = makeKey(source, destination, timestamp);

        if (packetSet.find(key) != packetSet.end())
        {
            return false;
        }

        if (checkLimit == memoryLimit)
            isLimit = true;

        if (isLimit)
        {
            if (!router.empty())
            {
                string oldKey = makeKey(router[0][0], router[0][1], router[0][2]);
                packetSet.erase(oldKey);
                router.erase(router.begin());
            }

            for (auto it = destinaitonCheck.begin(); it != destinaitonCheck.end();)
            {
                auto &values = it->second;

                values.erase(
                    remove_if(values.begin(), values.end(),
                              [](int &val)
                              {
                                  val -= 1;
                                  return val < 0;
                              }),
                    values.end());

                if (values.empty())
                {
                    it = destinaitonCheck.erase(it);
                }
                else
                {
                    ++it;
                }
            }

            destinaitonCheck[destination].push_back(memoryLimit - 1);
        }
        else
        {
            destinaitonCheck[destination].push_back(checkLimit);
            checkLimit += 1;
        }

        packetSet.insert(key); // 추가: packetSet에 삽입
        router.push_back({source, destination, timestamp});
        return true;
    }

    vector<int> forwardPacket()
    {
        if (router.empty())
            return {};

        vector<int> answer = router[0];

        string key = makeKey(answer[0], answer[1], answer[2]);
        packetSet.erase(key);

        router.erase(router.begin());

        for (auto &pair : destinaitonCheck)
        {
            auto &indices = pair.second;
            indices.erase(
                remove_if(indices.begin(), indices.end(),
                          [](int &val)
                          {
                              val -= 1;
                              return val < 0;
                          }),
                indices.end());
        }
        checkLimit -= 1;

        return answer;
    }

    int getCount(int destination, int startTime, int endTime)
    {
        if (destinaitonCheck.find(destination) == destinaitonCheck.end())
            return 0;

        vector<int> index = destinaitonCheck[destination];
        int answer = 0;

        for (auto i : index)
        {
            if (i >= 0 && i < router.size() &&
                startTime < router[i][2] && router[i][2] < endTime) // 수정: && 사용
            {
                answer += 1;
            }
        }
        return answer;
    }
};