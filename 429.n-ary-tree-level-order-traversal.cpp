/*
 * @lc app=leetcode id=429 lang=cpp
 *
 * [429] N-ary Tree Level Order Traversal
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
//#include <queue>
//using std::queue;
//#include <vector>
//using std::vector;
//
//class Node {
//public:
//    int val;
//    vector<Node*> children;
//
//    Node() {}
//
//    Node(int _val) {
//        val = _val;
//    }
//
//    Node(int _val, vector<Node*> _children) {
//        val = _val;
//        children = _children;
//    }
//};

class Solution {
public:
    vector<vector<int> > levelOrder(Node* root) {
        queue<Node*> q;
        vector<vector<int> > res;
        if (root) q.push(root);
        while (!q.empty()) {
            int size = q.size();
            vector<int> curRes;
            for (int i = 0; i != size; ++i) {
                Node* cur = q.front();
                q.pop();
                curRes.push_back(cur->val);
                for (vector<Node*>::iterator itr = cur->children.begin(); itr != cur->children.end(); ++itr) {
                    q.push(*itr);
                }
            }
            res.push_back(curRes);
        }
        return res; 
    }
};
// @lc code=end

