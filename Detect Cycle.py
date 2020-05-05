

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def checkpl(pl, x):
    for i in pl:
        if x==i:
            return 1
    return 0

def has_cycle(head):
    x=head
    pl=[]
    while x is not None:
        pl.append(x)
        x=x.next
        if checkpl(pl, x):
            return 1
    return 0

