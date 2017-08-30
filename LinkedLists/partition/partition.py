"""
    Partition : Write code to partition a linked list around a value x, such that all nodes
    less than x come before all nodes greater than or equal to x.If x is contained within
    the list , the value of x only need to be after the elements less than x (see below).
    The partition element x can appear anywhere in the "right partition" ; it does not need to
    appear between the left and right partitions

"""

from LinkedLists.LinkedList import LinkedList

def partition(linked_list:LinkedList, val:int):
    tll = LinkedList()
    head = linked_list.head
    while head is not None:
        if head.data < val:
            tll.add_to_beginning(head.data)
        else:
            tll.add(head.data)

        head = head.next

    linked_list.head = tll.head
    linked_list.tail = tll.tail





ll = LinkedList([3,5,8,5,10,2,1])
partition(ll, 5)
print(ll)
