/*
 * @lc app=leetcode id=59 lang=cpp
 *
 * [59] Spiral Matrix II
 */

// @lc code=start
//#include <vector>
//using std::vector;
class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        vector<vector<int> > ret(n, vector<int>(n));
        int startx = 0;
        int starty = 0;
        int loop = n / 2;
        int mid = n / 2;
        int count = 1;
        int offset = 1;
        int i, j;
        while (loop--) {
            i = startx;
            j = starty;
            for(; i < n - offset; ++i)
                ret[j][i] = count++;
            for(; j < n - offset; ++j)
                ret[j][i] = count++;
            for(; i >= offset; --i)
                ret[j][i] = count++;
            for(; j >= offset; --j)
                ret[j][i] = count++;
            ++startx;
            ++starty;
            ++offset;
        }
        if (n % 2 == 1)
            ret[mid][mid] = count;
        return ret; 
    }
};
// @lc code=end

