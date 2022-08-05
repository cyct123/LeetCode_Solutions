/*
 * @lc app=leetcode id=107 lang=cpp
 *
 * [107] Binary Tree Level Order Traversal II
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
//#include <queue>
//using std::queue;
//#include <algorithm>
//using std::reverse;
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
    vector<vector<int> > levelOrderBottom(TreeNode* root) {
        queue<TreeNode*> q;
        if (root) q.push(root);
        vector<vector<int> > res;
        while (!q.empty()) {
            vector<int> curRes;
            int size = q.size();
            for (int i = 0; i != size; ++i) {
                TreeNode* cur = q.front();
                q.pop();
                curRes.push_back(cur->val);
                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
            }
            res.push_back(curRes);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
// @lc code=end

