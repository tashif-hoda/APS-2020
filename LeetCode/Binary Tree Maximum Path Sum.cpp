/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int mps;
    int maxPathSum(TreeNode* root) {
        mps=-99999;
        pathsum(root);
        return mps;
    }
    
    int pathsum(TreeNode* node)
    {
        if(node==NULL) return 0;
        int l = max(0, pathsum(node->left));
        int r = max(0, pathsum(node->right));
        mps = max(mps, l + r + node->val);
        return max(l, r) + node->val;
    }
};
