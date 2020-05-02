/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution{
	public ListNode reverseBetween(ListNode head , int start , int end){
			if(head == null) {
				return null;
            }
			if(start > end){
                return head;
            }

			ListNode temp = head;
			int count = 0;
			ListNode prev = null;

			while(temp != null && count != start-1){
				prev = temp;
				temp = temp.next;
				count++;
			}

			ListNode connector = prev;
			ListNode tail = temp;


			// now temp is at start 
			// iterative reverse till curr.data == end 
			count = 0;
			ListNode third = null;
			while(count != end-start + 1){
				third = temp.next; 
				temp.next = prev ;
				prev = temp;
				temp = third;
				count++;
	        }
  			
  			// final adjustments 
  			if(connector != null) {
  				connector.next = prev;
  			} else {
  				head = prev;
  			}

  			tail.next = temp;
  			return head;
   }
}