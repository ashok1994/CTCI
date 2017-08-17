"""
    Return Kth to Last : Implement an algorithm to find the kth to last element of a singly linked list
"""

from LinkedLists.LinkedList import LinkedList,Node


def return_kth_to_last(linked_list:LinkedList, k:int):
    first = second = linked_list.head
    count = 0
    while count < k:
        second = second.next
        count+=1

    while second:
        second = second.next
        first = first.next

    return first.data




ll = LinkedList([1,2,3,4,5,6])
print(ll)
print(3,return_kth_to_last(ll,3))

ll = LinkedList()
ll.generate(10, 9,45)
print(ll)
print(4,return_kth_to_last(ll,4))


