/*
 * @lc app=leetcode id=347 lang=cpp
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
#include <vector>
using std::vector;
#include <queue>
using std::priority_queue;
#include <unordered_map>
using std::unordered_map;
#include <utility>
using std::pair;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> numsCount;
        for (vector<int>::iterator itr = nums.begin(); itr != nums.end(); ++itr)
            ++numsCount[*itr];
        auto comparePair = [](pair<int, int>left, pair<int, int> right){
            return left.second > right.second;
        }; 
        priority_queue<pair<int, int>, vector<pair<int, int> >, decltype(comparePair)> pq(comparePair);
        for (unordered_map<int, int>::iterator itr = numsCount.begin(); itr != numsCount.end(); ++itr) {
            pq.push(*itr);
            if (pq.size() > k)
                pq.pop();
        }
        vector<int> res;
        for (int i = 0; i != k; ++i){
            res.push_back(pq.top().first);
            pq.pop();
        }
        return res;
    }
};
// @lc code=end

