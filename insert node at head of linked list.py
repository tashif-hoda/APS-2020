
# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    x=SinglyLinkedListNode(data)
    x.next=llist
    llist=x
    return llist
    # Write your code here
