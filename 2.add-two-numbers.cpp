/*
 * @lc app=leetcode id=2 lang=cpp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
//#include <cstddef>
//using namespace std;
//struct ListNode {
//    int val;
//    ListNode *next;
//    ListNode() : val(0), next(nullptr) {}
//    ListNode(int x) : val(x), next(nullptr) {}
//    ListNode(int x, ListNode *next) : val(x), next(next) {}
//};
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        int carry = 0;
        while(l1 || l2 || carry){
            int l1Value = l1 ? l1->val: 0;
            int l2Value = l2 ? l2->val: 0;
            int value = l1Value + l2Value + carry;
            carry = value / 10;
            cur->next = new ListNode(value % 10);
            cur = cur->next;
            l1 = l1? l1->next: nullptr;
            l2 = l2? l2->next: nullptr;
        }
        return dummy->next;
    }
};
// @lc code=end

