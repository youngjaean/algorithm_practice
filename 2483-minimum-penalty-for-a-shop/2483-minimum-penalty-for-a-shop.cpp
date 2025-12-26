class Solution {
public:
    int bestClosingTime(string customers) {
        int yCount = count(customers.begin(), customers.end(), 'Y');
        int nCount = 0;

        int penalty = yCount;
        int minPenalty = penalty;
        int answer = 0;

        for (int i = 1 ; i <= customers.size(); i++)
        {
            switch(customers[i  - 1]){
                case 'Y':
                    penalty --;
                    break;
                case 'N':
                    penalty ++;
                    break;
            }
            if (minPenalty > penalty)
                {
                    minPenalty =  penalty;
                    answer = i;
                }
            
        } 
        return answer;
    }
};