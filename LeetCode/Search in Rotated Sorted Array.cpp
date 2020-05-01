class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0, h=nums.size()-1;
        return search(nums, l,h,target);
    }
    int search(vector<int>& arr, int l, int h, int key) 
    {
        if (l > h) return -1; 
        int mid = l+(h-l)/2; 
        if (arr[mid] == key) return mid; 
        if (arr[l] <= arr[mid]) 
        { 
            if (key >= arr[l] and key <= arr[mid]) 
            return search(arr, l, mid-1, key); 
            return search(arr, mid+1, h, key); 
        } 
        if (key >= arr[mid] && key <= arr[h]) 
            return search(arr, mid+1, h, key); 
        return search(arr, l, mid-1, key); 
    }
};
