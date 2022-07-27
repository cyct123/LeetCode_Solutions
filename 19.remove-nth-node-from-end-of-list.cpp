/*
 * @lc app=leetcode id=19 lang=cpp
 *
 * [19] Remove Nth Node From End of List
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* prev = new ListNode(-1, head);
        ListNode* slow = prev;
        ListNode* fast = slow;
        while (n != 0) {
            fast = fast->next;
            --n;
        }
        while (fast->next){
            slow = slow->next;
            fast = fast->next;
        }
        ListNode* deletedNode = slow->next;
        slow->next = deletedNode->next;
        deletedNode->next = nullptr;
        delete deletedNode;
        return prev->next;
    }
};
// @lc code=end

