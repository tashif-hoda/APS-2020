

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reversePrint(head):
    if head is not None:
        reversePrint(head.next)
        print(head.data)
    return
