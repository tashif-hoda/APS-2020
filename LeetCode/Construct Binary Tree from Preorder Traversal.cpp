/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int preind=0;
        return construct(preorder, &preind, 0, preorder.size()-1, preorder.size());
        
    }
    
    TreeNode* construct(vector<int>& pre, int* preIndex, int low, int high, int size)
    {  
        if (*preIndex >= size || low > high)  
            return NULL;  
        TreeNode* root = new TreeNode;
        root->val = pre[*preIndex];  
        *preIndex = *preIndex + 1;  

        if (low == high)  
            return root;  

        int i;  
        for (i = low; i <= high; ++i)  
            if (pre[i] > root->val)  
                break;  

        root->left = construct(pre, preIndex, *preIndex, i - 1, size);  
        root->right = construct(pre, preIndex, i, high, size);  

        return root;  
    }  
};
