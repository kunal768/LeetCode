// Long Method : Counting from beginning (check size also)
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null || head.next == null||k == 0){
            return head;
        }
        int size = 0 ;
        ListNode temp = head;
        ListNode prev = null;
        while(temp != null){
            size++;
            prev = temp;
            temp = temp.next;
        }
        
        // join from back 
        prev.next = head;
        
        // rotate count
        int rc = 0;
        if (size > k){
            rc = size - k;
        } else {
            rc = size - k%size;
        }       
        
        prev = null;
        temp = head;    
        
        while((temp != null) && (rc > 0)){
            rc--;
            prev = temp;
            temp = temp.next;
        }
        
        
        ListNode ans = prev.next;
        prev.next = null;
        return ans;
    }
}
