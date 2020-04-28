class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> umap;
        int s=0, largest_diff=0;
        for(int i=0; i<nums.size(); i++)
        {
            if (!nums[i])
                s+=-1;
            else
                s+=1;
            
            if (!s)
                largest_diff=i+1;
            
            else if(umap.find(s)!=umap.end())
            {
                if(i - umap[s] > largest_diff)
                    largest_diff = i - umap[s];
            }
            else
            {
                umap[s]=i;
            }
        }

        return largest_diff;
    }
};
