/*
 * @lc app=leetcode id=203 lang=cpp
 *
 * [203] Remove Linked List Elements
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
//struct ListNode {
//    int val;
//    ListNode *next;
//    ListNode() : val(0), next(nullptr) {}
//    ListNode(int x) : val(x), next(nullptr) {}
//    ListNode(int x, ListNode *next) : val(x), next(next) {}
//};

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* prev = new ListNode(0, head);
        ListNode* dummy = prev;
        while (prev->next) {
            ListNode* curNode = prev->next;
            if (curNode->val == val) {
                prev->next = curNode->next;
                curNode->next = nullptr;
            } else {
                prev = prev->next;
            }
        }
        return dummy->next;
    }
};
// @lc code=end

