/*
 * @lc app=leetcode id=232 lang=cpp
 *
 * [232] Implement Queue using Stacks
 */

// @lc code=start
#include <vector>
using std::vector;
class MyQueue {
public:
    MyQueue() {
    }
    
    void push(int x) {
        pushVector.push_back(x); 
    }
    
    int pop() {
        while (pushVector.size() > 1) {
            popVector.push_back(pushVector.back());
            pushVector.pop_back();
        }
        int val = pushVector.back();
        pushVector.pop_back();
        while (popVector.size()) {
            pushVector.push_back(popVector.back());
            popVector.pop_back();
        }
        return val;
    }
    
    int peek() { 
        return pushVector.front();
    }
    
    bool empty() {
        return pushVector.empty();
        
    }
private:
    vector<int> pushVector;
    vector<int> popVector; 
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
// @lc code=end

