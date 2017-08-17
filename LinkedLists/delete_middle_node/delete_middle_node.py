"""
    Delete Middle Node : Implement an algorithm to delete a node in the middle (i.e., any node but the first and the last
    node, not necessarily the exact middle) of a singly linked list , given only access to the node

    EXAMPLE
    Input the node c from the linked list a->b->c->d->e->f
    Result: nothing is returned , but the new linked list looks like a->b->d->e->f

"""


from LinkedLists.LinkedList import LinkedList,Node


def delete_middle_node(linked_list:LinkedList, node:Node):
    curr = linked_list.head
    while curr.next != None:
        if curr.next is node:
            curr.next = node.next
        else:
            curr = curr.next



ll = LinkedList([1,2,3,4,5])

curr = ll.head

delete_middle_node(ll,curr.next.next.next.next)

print(ll)

