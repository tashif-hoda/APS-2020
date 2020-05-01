class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if(matrix.empty())
            return 0;
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        int dpmax=0;
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i+1][j+1] = (matrix[i][j]=='0')? 0 : min({dp[i][j], dp[i][j+1], dp[i+1][j]})+1;
                dpmax = max(dpmax, dp[i+1][j+1]);
            }
        }
        return dpmax*dpmax;
    }
};
