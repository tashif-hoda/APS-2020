

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    x=head
    tp=None
    while head != None:
        if head.data<data:
            tp=head
            head=head.next
        else:
            k=DoublyLinkedListNode(data)
            k.prev=head.prev
            if k.prev is None:
                k.next=head
                head.prev=k
                return k
            # print(k.prev.data)
            head.prev=k
            k.prev.next=k
            k.next=head
            return x
    head=tp
    head.next=DoublyLinkedListNode(data)
    head.next.prev = head
    return x

