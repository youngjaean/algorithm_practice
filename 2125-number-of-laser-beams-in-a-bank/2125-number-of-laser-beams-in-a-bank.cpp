class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int count= 0 , prev = 0, ans = 0;

        for (auto laz : bank)
        {
            count = 0;
            for (int i = 0; i < laz.size(); i++)
            {
                if (laz[i] == '1') 
                    count ++;
            }
            if (count){
                ans += prev * count;
                prev  = count;
            }
        }
        return ans;
        
    }
};