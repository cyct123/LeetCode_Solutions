/*
 * @lc app=leetcode id=27 lang=cpp
 *
 * [27] Remove Element
 */

// @lc code=start
//#include <vector>
//#include <iostream>
//#include <iterator>
//#include <algorithm>
//using std::copy;
//using std::ostream_iterator;
//using std::endl;
//using std::cout;
//using std::vector;
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slowIndex = 0;
        for(int fastIndex = 0; fastIndex != nums.size(); ++fastIndex){
            if(val != nums[fastIndex])
                nums[slowIndex++] = nums[fastIndex];
        }
        return slowIndex;
    }
};

//int main() {
//    vector<int> nums{3, 2, 2, 3};
//    int val = 3;
//    Solution s = Solution();
//    int len = s.removeElement(nums, val);
//    cout << len << endl;
//    copy(nums.begin(), nums.end(), ostream_iterator<int>(cout, " "));
//    return 0; 
//}
// @lc code=end

