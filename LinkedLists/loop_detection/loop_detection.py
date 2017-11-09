"""
    Given a circular, implement an algorithm that returns at the node
    at the beginning of the loop.

    DEFINITION:
    Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier
    node, so as to make a loop in the linked list.

    EXAMPLE:
    Input: A -> B -> C -> D -> E -> C [the same C as earlier]

    Output: C
"""

from LinkedLists.LinkedList import LinkedList

def detect_cycle_node(ll):
    slow = ll.head
    fast = ll.head
    while slow and fast:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    # if loop broke because it reached none condition (i.e. either fast is none or slow is none)
    if fast is None or fast.next is None:
        return None

    # finding the starting node
    slow = ll.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return fast


l1 = LinkedList()
l1.add(1)
l1.add(2)
l1.add(3)
node = l1.add(4)
l1.add(5)
l1.add(6)
l1.add(7)

l1.tail.next = node

print(detect_cycle_node(l1))


