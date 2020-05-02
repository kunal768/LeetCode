// this is the first time (fuck! not the first time)
// but it happens to be a medium question on LeetCode and i fucking forgot we could use two pointers
// to solve this ya ... so here's the better solution 

// my brute - accepted solution... i thought about writing it ... but fuck it this is better

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        if(head == null || head.next == null) return null;
        
        ListNode hare = head;
        ListNode turtle = head;
   
        // set this bitch ahead
        for(int i = 0; i <n;i++){
            hare = hare.next;
            if(hare == null){return head.next;}
        }      
        
        // now keep traversing all shit .. hare,turtle and ya keep a prev pointer to delete  turtle
        
        while((hare!=null) && (turtle !=null)){
            turtle = turtle.next;
            hare = hare.next;
        }
        // hare reached the end so the node to be deleted is turtle
   		hare.next = hare.next.next;
   		
        return head;
    
    }
        
}