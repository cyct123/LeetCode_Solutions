/*
 * @lc app=leetcode id=160 lang=cpp
 *
 * [160] Intersection of Two Linked Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//#include <cstddef>
//struct ListNode {
//    int val;
//    ListNode *next;
//    ListNode(int x) : val(x), next(NULL) {}
//};
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curA = headA;
        ListNode* curB = headB;
        int lenA = 0;
        int lenB = 0;
        while (curA) {
            curA = curA->next;
            ++lenA;
        }
        while (curB) {
            curB = curB->next;
            ++lenB;
        }
        if (lenA > lenB) {
            for (int i = 0; i != lenA - lenB; ++i) headA = headA->next;   
        }
        else if (lenA < lenB){
            for (int i = 0; i != lenB - lenA; ++i) headB = headB->next;
        }
        while (headA && headB) {
            if (headA == headB) return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return NULL;
    }
};
// @lc code=end

