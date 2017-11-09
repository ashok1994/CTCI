"""
    Given two (singly) linked lists , determine if the two lists interact . Return the intersecting node.
    Note that the intersection is defined based on reference , not value. That is, if the kth node of
    the first linked list is the exact same node (by reference) as the jth node of the second linked list,
    then they are intersecting.
"""

from LinkedLists.LinkedList import LinkedList

def get_intersecting_node(ll1, ll2):
    head1 = ll1.head
    while head1:
        head2 = ll2.head
        while head2:
            if head1 is head2:
                return head1
            else:
                head2 = head2.next
        head1 = head1.next
    return False




l1 = LinkedList()

l1.add(1)
l1.add(2)
node = l1.add(3)
l1.add(4)


l2 = LinkedList()
l2.add(11)
l2.add(12)
l2.add(13)

l2.tail.next = node
l2.tail = node

print(get_intersecting_node(l1, l2))

