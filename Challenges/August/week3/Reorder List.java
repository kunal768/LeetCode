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
 // ProTip : ALWAYS USE JAVA FOR LINKED LIST QUESTIONS AS PYTHON IS A FUCKALL LANGUAGE FOR LINKED LISTS
 
class Solution {
    public ListNode reverse(ListNode node){
        if(node == null || node.next == null){
            return node;
        }
        ListNode next = null;
        ListNode curr = node;
        ListNode prev = null; //,prev = null,node,null;
        while (curr != null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    
    
    public void reorderList(ListNode node) {
        if(node == null || node.next == null){
            return ;
        } 
        
        ListNode slow = node;
        ListNode fast = node;
        ListNode prev = null;
        while(fast!= null && fast.next != null){
            fast = fast.next.next;
            prev = slow;
            slow = slow.next;
        }
        
        
        prev.next = null;
        ListNode second = reverse(slow);
        ListNode temp = new ListNode(0);
        ListNode ans = temp;
        while (node != null && second != null){
            ans.next = node;
            ans = ans.next;
            node = node.next;
            ans.next = second;
            ans = ans.next;
            second = second.next;
        }
        
        if(node != null){
            ans.next = node;
        }
        
        if(second != null){
            ans.next = second;
        }
        
        
        node = temp.next;
    }
}
