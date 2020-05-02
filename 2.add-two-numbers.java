/*
 * @lc app=leetcode id=2 lang=java
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (32.05%)
 * Likes:    6218
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
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int adder = 0;
        ListNode l = new ListNode(0);
        ListNode dummy = l;
        while ((l1 != null) || (l2 != null) || (adder != 0)) {
            int valL1 = (l1 == null) ? 0: l1.val;
            int valL2 = (l2 == null) ? 0: l2.val;
            int plus = valL1 + valL2 + adder;
            adder = plus / 10;
            plus = plus % 10;
            l.next = new ListNode(plus);
            l = l.next;
            l1 = (l1 != null) ? l1.next: null;
            l2 = (l2 != null) ? l2.next: null;
        }
        return dummy.next;
    }
}
// @lc code=end

