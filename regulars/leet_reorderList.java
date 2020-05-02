class Solution{
	public ListNode reverse(ListNode curr){
		if(curr == null){
			return curr;
		}
		ListNode prev = null;
		ListNode temp = null;

		while(curr != null){
			temp = curr.next;
			curr.next = prev;
			prev = curr;
			curr = temp;
		}
		return prev;
	}
	
	public void merge(ListNode l1 , ListNode l2){
		while(l1 != null){
			ListNode l1_next = l1.next;
			ListNode l2_next = l2.next;

			l1.next = l2;
			if(l1_next == null){
				break;
			}
			l2.next = l1_next;
			l1 = l1_next;
			l2 = l2_next;

		}
	}

	public void reorderList(ListNode head){
		if(head == null || head.next == null){
			return;
		}
		// head of first half
		ListNode l1 = head;
	    // tail of second half
		ListNode fast = head;
		// head of second half
		ListNode slow = head;
		// tail of first half
		ListNode prev = null;
		
		while(fast != null && fast.next != null){
 				prev = slow;
 				fast = fast.next.next;
 				slow = slow.next;
		}
 
		prev.next = null;

		ListNode l2 = reverse(slow);

		merge(l1,l2);

	}
}

