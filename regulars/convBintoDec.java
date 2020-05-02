// https://leetcode.com/tag/linked-list/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverse(ListNode root){
        if(root == null || root.next == null){
            return root;
        }
        ListNode revHead = reverse(root.next);
        root.next.next = root;
        root.next = null;
        return revHead;
    }
    public int getDecimalValue(ListNode head) {
        head = reverse(head);
        if(head.next == null){
            return head.val;
        }
        int c = 0;
        int sum = 0;
        while(head != null){
            sum += Math.pow(2,c)*head.val;
            // System.out.println(sum);
            c++;
            head = head.next;
        }
    
        return sum;
    }
}