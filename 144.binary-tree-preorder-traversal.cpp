/*
 * @lc app=leetcode id=144 lang=cpp
 *
 * [144] Binary Tree Preorder Traversal
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
#include <vector>
using std::vector;
#include <stack>
using std::stack;
#include <unordered_set>
using std::unordered_set;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if(!root) return res;
        stack<TreeNode*> s;
        s.push(root);
        unordered_set<TreeNode*> visited;
        while (!s.empty()) {
            TreeNode* cur = s.top();
            visited.insert(cur);
            s.pop();
            res.push_back(cur->val);
            if(cur->right && !visited.count(cur->right))
                s.push(cur->right);
            if(cur->left && !visited.count(cur->left))
                s.push(cur->left);
        }
        return res;
    }
};
// @lc code=end
