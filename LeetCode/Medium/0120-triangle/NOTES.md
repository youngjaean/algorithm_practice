allaways j, i is +1 i will find minimum sum.
​
Exceptions is triangle length is 1
​
and memorization. for example
min(2 + 3 =5 , 2+4= 6 ) show the resulte
​
위와 같이 풀면  그리드가 됨.  당장 작은 것을 선택하기때문에 가장 작은것이 될 수 없음
​
Tabluation 을 이용하기.
​
bottom up DP 이기때문에 가장 밑에부터 시작해보자
즉
​
4,1,8,3 중 가장 작은것을 고 르고
6,5,7 중 1에서 갈 수 있는 모든것들을 저장 [7,6] 그리고 7이 갈 수있는 가장 작은 숫자 3과 결합하여
[7,6,10] 을 통해 후보군을 하나 추가한다 이를 반복
​
Tabluation의 기본 개념부터 이해하면 DP에 다양하게 적용가능하다.
​
​
​