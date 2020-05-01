class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n,checkpoint;
        n=checkpoint=nums.size()-1;
        for(int i=n; i>-1; i--)
            if(nums[i] + i >= checkpoint)
                checkpoint = i;
        
        return checkpoint==0;
    }
};
