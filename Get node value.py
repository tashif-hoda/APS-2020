

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    a = head
    b = head
    c = 0
    while a is not None:
        a = a.next
        if c>positionFromTail:
            b=b.next
        c+=1
    return b.data


