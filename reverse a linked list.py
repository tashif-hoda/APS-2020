

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    if head==None or head.next==None:
        return head
    rem = reverse(head.next)
    head.next.next = head
    head.next = None
    return rem
    

