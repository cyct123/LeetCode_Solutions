/*
 * @lc app=leetcode id=94 lang=cpp
 *
 * [94] Binary Tree Inorder Traversal
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
//#include <stack>
//using std::stack;
//#include <unordered_set>
//using std::unordered_set;
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res; 
        if (!root) return res;
        unordered_set<TreeNode*> visited;
        stack<TreeNode*> s;
        s.push(root);
        while (!s.empty()) {
            TreeNode* cur = s.top();
            visited.insert(cur);
            if (cur->left && !visited.count(cur->left)) {
                s.push(cur->left);
                continue;
            }
            res.push_back(cur->val);
            s.pop();
            if(cur->right && !visited.count(cur->right))
                s.push(cur->right);
        }
        return res;
    }
};
// @lc code=end

