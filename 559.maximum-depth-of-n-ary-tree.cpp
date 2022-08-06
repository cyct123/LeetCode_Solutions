/*
 * @lc app=leetcode id=559 lang=cpp
 *
 * [559] Maximum Depth of N-ary Tree
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
    int maxDepth(Node* root) {
       int depth = 0;
       if (!root) return depth;
       queue<Node*> q;
       q.push(root);
       maxDepth(q, depth);
       return depth;
    }
private:
    void maxDepth(queue<Node*>& q, int& depth) {
        if (q.empty()) return;
        ++depth;
        int size = q.size();
        for (int i = 0; i != size; ++i) {
            Node* cur = q.front(); q.pop();
            for (vector<Node*>::iterator itr = cur->children.begin(); itr != cur->children.end(); ++itr)
                q.push(*itr);
        }
        maxDepth(q, depth);
    }
};
// @lc code=end

