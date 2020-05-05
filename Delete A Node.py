

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    temp = head

    if not position:
        return temp.next
    else:
        for _ in range(position-1):
            temp=temp.next
        temp.next = temp.next.next
        return head

