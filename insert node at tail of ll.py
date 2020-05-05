

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if head == None:
        return SinglyLinkedListNode(data)
        #print(head)
    temp = head
    #print(temp)
    while temp!=None:
        prevfinal = temp
        temp=temp.next
        #print(prevfinal)
    prevfinal.next = SinglyLinkedListNode(data)
    return head


