

# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    x = head
    while x.next is not None:
        if x.data == x.next.data:
            x.next = x.next.next
            continue
        x = x.next
    return head
        

