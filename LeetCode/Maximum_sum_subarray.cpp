class Solution {
public:
    
    long long int max(long long int a, long long int b)
    {
        return a>b?a:b;
    }
    
    int maxSubArray(vector<int>& nums) {
        long long int best_sum=INT_MIN;
        long long int curr_sum=0;
        for(auto i=nums.begin(); i<nums.end();i++)
        {
            curr_sum=max(*i, curr_sum + *i);
            best_sum=max(curr_sum, best_sum);
        }
        
        return best_sum;
    }
};
