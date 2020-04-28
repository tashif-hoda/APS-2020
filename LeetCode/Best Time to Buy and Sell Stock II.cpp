class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lmin, lmax;
        int profit=0;
        int i=0;
        int n=prices.size();
        while(i<n-1)
        {
            while(i<n-1 and prices[i+1]<=prices[i])
                i++;
            lmin=prices[i++];
            while(i<n and prices[i-1]<=prices[i])
                i++;
            lmax=prices[i-1];
            profit+=lmax-lmin;
        }
        return profit;
    }
};
