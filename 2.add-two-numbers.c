/*
 * @lc app=leetcode id=2 lang=c
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (32.05%)
 * Likes:    6215
 * Dislikes: 1620
 * Total Accepted:    1.1M
 * Total Submissions: 3.3M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order and each of their nodes
 * contain a single digit. Add the two numbers and return it as a linked list.
 *
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 *
 * Example:
 *
 *
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 * Explanation: 342 + 465 = 807.
 *
 *
 */

// @lc code=start
/*
 *Definition for singly-linked list.
 *struct ListNode {
 *    int val;
 *    struct ListNode *next;
 *};
 */
//#include <stdio.h>


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *head, *cur;
    int sum, val1, val2, carrier = 0;
    while (l1 || l2 || carrier) {
        struct ListNode *dummy = (struct ListNode *) malloc(sizeof(struct ListNode));
        if (head == NULL)
            head = cur = dummy;
        else {
            cur->next = dummy;
            cur = cur->next;
        }
        val1 = (l1 == NULL) ? 0 : l1->val;
        val2 = (l2 == NULL) ? 0 : l2->val;
        sum = val1 + val2 + carrier;
        carrier = sum / 10;
        sum %= 10;
        cur->val=sum;
        if (l1)
            l1 = l1->next;
        if (l2)
            l2 = l2->next;
    }
    return head;
}


// @lc code=end

