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
//#include <algorithm>
//using std::max;
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
        if (!root) return 0;
        int subMaxDepth = 0;
        for (vector<Node*>::iterator itr = root->children.begin(); itr != root->children.end(); ++itr) {
            int subDepth = maxDepth(*itr);
            subMaxDepth = subMaxDepth > subDepth ? subMaxDepth: subDepth;
        }
        return ++subMaxDepth;
    }
};
// @lc code=end

