class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        double maxArea = 0.0;
        int n = points.size();
        
        // 모든 세 점의 조합을 확인
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    // 세 점으로 삼각형 넓이 계산
                    // 넓이 = 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
                    double area = 0.5 * abs(
                        points[i][0] * (points[j][1] - points[k][1]) +
                        points[j][0] * (points[k][1] - points[i][1]) +
                        points[k][0] * (points[i][1] - points[j][1])
                    );
                    
                    maxArea = max(maxArea, area);
                }
            }
        }
        
        return maxArea;
    }
};