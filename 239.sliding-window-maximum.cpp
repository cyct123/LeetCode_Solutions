/*
 * @lc app=leetcode id=239 lang=cpp
 *
 * [239] Sliding Window Maximum
 */

// @lc code=start
#include <vector>
using std::vector;
#include <deque>
using std::deque;

class MyQueue {
    public:
        void pop(int x){
            if (!dq.empty() && dq.front() == x)
                dq.pop_front();
        }

        void push(int x){
            while (!dq.empty() && x > dq.back())
                dq.pop_back();
            dq.push_back(x);
        }

        int front() {
            return dq.front();
        }
    private:
        deque<int> dq;
};

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        MyQueue q;
        for (int i = 0; i != nums.size() - k + 1; ++i) {
            if (!i) {
                for (int j = 0; j != k; ++j){
                    q.push(nums[i+j]);
                }
            } else {
                q.pop(nums[i-1]);
                q.push(nums[i+k-1]);
            }
            res.push_back(q.front());
        }
        return res;
    }
};
// @lc code=end

