/*
 * @lc app=leetcode id=225 lang=cpp
 *
 * [225] Implement Stack using Queues
 */

// @lc code=start
#include <queue>
using std::queue;


class MyStack {
public:
    MyStack() {
        
    }
    
    void push(int x) {
        pushQueue.push(x);
    }
    
    int pop() {
        while (pushQueue.size() > 1) {
            popQueue.push(pushQueue.front());
            pushQueue.pop();
        }
        int val = pushQueue.front();
        pushQueue.pop();
        pushQueue = popQueue;
        while (popQueue.size()) popQueue.pop();
        return val;
    }
    
    int top() {
        return pushQueue.back(); 
    }
    
    bool empty() {
        return pushQueue.empty(); 
    }
private:
    queue<int> pushQueue;
    queue<int> popQueue;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
// @lc code=end

