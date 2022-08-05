/*
 * @lc app=leetcode id=102 lang=cpp
 *
 * [102] Binary Tree Level Order Traversal
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
    vector<vector<int> > levelOrder(TreeNode* root) {
        vector<TreeNode*> curLevel;
        vector<TreeNode*> nextLevel;
        vector<vector<int> > res;
        if(root) curLevel.push_back(root);
        while (!curLevel.empty()) {
            vector<int> curRes;
            for (vector<TreeNode*>::iterator itr = curLevel.begin(); itr != curLevel.end(); ++itr) {
                curRes.push_back((*itr)->val);
                if ((*itr)->left) nextLevel.push_back((*itr)->left);
                if ((*itr)->right) nextLevel.push_back((*itr)->right);
            }
            res.push_back(curRes);
            curRes.clear();
            curLevel = nextLevel;
            nextLevel.clear();
        } 
        return res;
    }
};
// @lc code=end

