

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    x = head
    y=None
    while x is not None:
        temp=x.next
        x.next = x.prev
        x.prev = temp
        y = x
        x = x.prev
    return y


