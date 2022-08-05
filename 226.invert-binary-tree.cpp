/*
 * @lc app=leetcode id=226 lang=cpp
 *
 * [226] Invert Binary Tree
 */

// @lc code=start
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
//struct TreeNode {
//    int val;
//    TreeNode *left;
//    TreeNode *right;
//    TreeNode() : val(0), left(nullptr), right(nullptr) {}
//    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
//};

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(!root) return root;        
        invert(root);
        return root;
    }
private:
    void invert(TreeNode* root) {
        if (!root) return;
        TreeNode* left = root->left;
        TreeNode* right = root->right;
        root->left = right;
        root->right = left;
        invert(root->left);
        invert(root->right);
    }
};
// @lc code=end

