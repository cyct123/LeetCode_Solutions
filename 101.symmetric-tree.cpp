/*
 * @lc app=leetcode id=101 lang=cpp
 *
 * [101] Symmetric Tree
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
//using std::vector;
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
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        vector<TreeNode*> st = {root->left, root->right}; 
        while (!st.empty()) {
            TreeNode* right = st.back();
            st.pop_back();
            TreeNode* left = st.back();
            st.pop_back();
            if (!left && !right) continue;
            if ((!left && right) || (left && !right)) return false;
            if (left && right && left->val != right->val) return false;
            st.push_back(left->left);
            st.push_back(right->right);
            st.push_back(left->right);
            st.push_back(right->left);
        }
        return st.empty();
    }
};
// @lc code=end

