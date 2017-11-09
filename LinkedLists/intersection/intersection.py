"""
    Given two (singly) linked lists , determine if the two lists interact . Return the intersecting node.
    Note that the intersection is defined based on reference , not value. That is, if the kth node of
    the first linked list is the exact same node (by reference) as the jth node of the second linked list,
    then they are intersecting.
"""

from LinkedLists.LinkedList import LinkedList

def get_node_uniform(head1, head2):
    while head1 is not head2:
        head1 = head1.next
        head2 = head2.next
    return head1


def adjust_head(n,head):
    while n != 0:
        head = head.next
        n-=1
    return head


def get_intersecting_node(ll1, ll2):
    len1 = len(ll1)
    len2 = len(ll2)
    if len1 == len2:
        return get_node_uniform(ll1.head,ll2.head)
    elif len2 > len1:
        head2 = adjust_head(len2 - len1 , ll2.head)
        return get_node_uniform(ll1.head, head2)
    else:
        head1 = adjust_head(len1 - len2, ll1.head)
        return get_node_uniform(head1, ll2.head)




l1 = LinkedList()

l1.add(1)
node = l1.add(2)
l1.add(3)
l1.add(4)


l2 = LinkedList()
l2.add(11)
l2.add(12)
l2.add(13)
l2.tail.next = node
l2.tail = l1.tail


print(get_intersecting_node(l1, l2))

