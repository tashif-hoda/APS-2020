class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        vector<int> out(n,1);
        int i=1, rev=1;
        while(i<n)
        {
            out[i++]=out[i-1]*nums[i-1];
        }
        while(--i>=0)
        {
            out[i]=out[i]*rev;
            rev*=nums[i];
        }
        return out;
    }
};
