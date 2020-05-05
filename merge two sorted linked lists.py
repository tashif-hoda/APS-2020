

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def swap(a, b):
    temp = a.data
    a.data = b.data
    b.data = temp

def mergeLists(head1, head2):
    x = head1
    while x.next is not None:
        x=x.next
    x.next = head2
    x = head1
    s=1
    t = None
    while s:
        s=0
        x=head1
        while x.next != t:
            if x.data>x.next.data:
                swap(x, x.next)
                s=1
            x = x.next
        t = x
    return head1
        




