/*
 * @lc app=leetcode id=222 lang=cpp
 *
 * [222] Count Complete Tree Nodes
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
//#include <queue>
//using std::queue;
//
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
    int countNodes(TreeNode* root) {
        if (!root) return 0;
        int leftHeight = 0;
        int rightHeight = 0;
        TreeNode* leftNode = root->left;
        TreeNode* rightNode = root->right;
        while (leftNode) {
            ++leftHeight;
            leftNode = leftNode->left;   
        }
        while (rightNode) {
            ++rightHeight;
            rightNode = rightNode->right;
        }
        if (leftHeight == rightHeight) return (2 << leftHeight) - 1;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
// @lc code=end

