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
        if (!left && !right) return true;
        if (!left || !right || left->val != right->val) return false;
        return isSameTree(left->left, right->left) && isSameTree(left->right, right->right);
    }
};
// @lc code=end

