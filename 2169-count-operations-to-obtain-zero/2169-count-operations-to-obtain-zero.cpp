class Solution {
public:
    int answer = 0 ;
    int countOperations(int num1, int num2) {
        
        if (num1 == 0 || num2 == 0 )
            return answer ;
        
        if (num1 >= num2)
        {    
            answer++;
            num1 -= num2;
        }
        else{
            answer++;
            num2 -= num1;
        }
        return countOperations(num1, num2);
        
        
    }
};