/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode merge(ListNode A,ListNode B){
        if(A == null){
            return B ;
        }
        if(B == null){
            return A;
        }
        if(A.val <= B.val){
            A.next = merge(A.next ,B);
            return A;
        }else{
            B.next = merge(A,B.next);
            return B;
        }    
    }
    
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null)
            return head;
            
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;
        
        while((fast != null) && (fast.next != null)){
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        prev.next = null;
        ListNode left = sortList(head);
        ListNode right = sortList(slow);
        
        return merge(left,right);
        
    }
    
}
