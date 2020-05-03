/*
 * @lc app=leetcode id=21 lang=java
 *
 * [21] Merge Two Sorted Lists
 *
 * https://leetcode.com/problems/merge-two-sorted-lists/description/
 *
 * algorithms
 * Easy (51.13%)
 * Likes:    3304
 * Dislikes: 490
 * Total Accepted:    835.9K
 * Total Submissions: 1.6M
 * Testcase Example:  '[1,2,4]\n[1,3,4]'
 *
 * Merge two sorted linked lists and return it as a new list. The new list
 * should be made by splicing together the nodes of the first two lists.
 *
 * Example:
 *
 * Input: 1->2->4, 1->3->4
 * Output: 1->1->2->3->4->4
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode l = new ListNode(0);
        ListNode cur = l;
        while (l1 != null || l2 != null) {
            int valL1 = (l1 == null) ? Integer.MAX_VALUE : l1.val;
            int valL2 = (l2 == null) ? Integer.MAX_VALUE : l2.val;
            ListNode node = new ListNode(valL1 < valL2 ? valL1: valL2);
            cur.next = node;
            cur = cur.next;
            if (valL1 < valL2) {
                l1 = l1.next;
            } else {
                l2 = l2.next;
            }
        }
        return l.next;
    }
}
// @lc code=end

