

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    x=SinglyLinkedListNode(data)
    #head = head.next
    temp = head
    for _ in range(position-1):
        temp=temp.next
    x.next=temp.next
    temp.next=x
    return head




