/*
 * @lc app=leetcode id=257 lang=cpp
 *
 * [257] Binary Tree Paths
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
//#include <string>
//using std::string;
//using std::to_string;
//#include <stack>
//using std::stack;
//
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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        stack<TreeNode*> treeSt;
        stack<string> pathSt;
        if (!root) return res;
        treeSt.push(root);
        pathSt.push(to_string(root->val));
        while (!treeSt.empty()) {
            TreeNode* curNode = treeSt.top(); treeSt.pop();
            string curPath = pathSt.top(); pathSt.pop();
            if (!curNode->left && !curNode->right)
                res.push_back(curPath);
            if (curNode->right) {
                treeSt.push(curNode->right);
                pathSt.push(curPath + "->" + to_string(curNode->right->val));
            }
            if (curNode->left) {
                treeSt.push(curNode->left);
                pathSt.push(curPath + "->" + to_string(curNode->left->val));
            } 
        }
        return res;
    }
    
};
// @lc code=end

