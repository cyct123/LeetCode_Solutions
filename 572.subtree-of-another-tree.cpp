/*
 * @lc app=leetcode id=572 lang=cpp
 *
 * [572] Subtree of Another Tree
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
//#include <vector>
//using std::vector;
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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root && subRoot) return false;
        if (root && !subRoot) return true;
        vector<TreeNode*> st = {root};
        while (!st.empty()) {
            TreeNode* cur = st.back(); st.pop_back();
            if (isSameTree(cur, subRoot)) return true;
            if (cur->left) st.push_back(cur->left);
            if (cur->right) st.push_back(cur->right);
        }
        return false;
    }
private:
    bool isSameTree(TreeNode* left, TreeNode* right) {
        vector<TreeNode*> st = {left, right};
        while (!st.empty()) {
            TreeNode* right = st.back(); st.pop_back();
            TreeNode* left = st.back(); st.pop_back();
            if (!left && !right) continue;
            if (!left || !right || left->val != right->val) return false;
            st.push_back(left->left);
            st.push_back(right->left);
            st.push_back(left->right);
            st.push_back(right->right);
        }
        return st.empty();
    }
};
// @lc code=end

