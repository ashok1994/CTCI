"""
    Delete Middle Node : Implement an algorithm to delete a node in the middle (i.e., any node but the first and the last
    node, not necessarily the exact middle) of a singly linked list , given only access to the node

    EXAMPLE
    Input the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned , but the new linked list looks like a->b->d->e->f

"""


from LinkedLists.LinkedList import LinkedList,Node


def delete_middle_node(node:Node):
    node.data = node.next.data
    node.next = node.next.next




ll = LinkedList([1,2,3,4,5])
middle = ll.add(6)
ll.add_multiple([1,2,3])

print(ll)
delete_middle_node(middle)

print(ll)

