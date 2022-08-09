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
        if (!root) return res;
        string path;
        traversal(root, path, res);
        return res;
    }
private:
    void traversal(TreeNode* cur, string path, vector<string>& res) {
        path += to_string(cur->val);
        if (!cur->left && !cur->right) {
            res.push_back(path);
            return;
        }
        if (cur->left) traversal(cur->left, path + "->", res);
        if (cur->right) traversal(cur->right, path + "->", res);
    }
    
};
// @lc code=end

