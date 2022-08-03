/*
 * @lc app=leetcode id=150 lang=cpp
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
#include <string>
#include <vector>
#include <iostream>
using std::stoi;
using std::string;
using std::vector;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> nums;
        string operators = "+-*/";
        for (vector<string>::iterator itr = tokens.begin(); itr != tokens.end(); ++itr) {
            if (operators.find(*itr) == string::npos)
                nums.push_back(stoi(*itr));
            else {
                int num1 = nums.back();
                nums.pop_back();
                int num2 = nums.back();
                nums.pop_back();
                nums.push_back(doMath(num1, num2, *itr));
            }
        }
        return nums.back(); 
    }
private:
    int doMath(int num1, int num2, string op) {
        if (op == "+") 
            return num1 + num2;
        else if (op == "-")
            return num2 - num1;
        else if (op == "*")
            return num1 * num2;
        else
            return num2 / num1;
    }
};
// @lc code=end

