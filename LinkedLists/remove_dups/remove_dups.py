"""
    Remove Dups :
    Write code to remove duplicate from an unsorted list. --> remove_dups()
    Follow up
    How would you solve this problem if a temporary buffer is not allowed ? --> remove_dups_b()
"""

from LinkedLists.LinkedList import LinkedList

def remove_dups(linked_list):
    memo = []
    curr = linked_list.head
    # First Value
    memo.append(curr.data)

    while curr.next is not None:
        if curr.next.data in memo:
            curr.next = curr.next.next
        else:
            memo.append(curr.next.data)
            curr = curr.next


def remove_dups_follow_up(linked_list):
    i = linked_list.head
    j = i

    while i is not None:
        while j is not None:
            if j.next:
                if j.next.data == i.data:
                    j.next = j.next.next
                else:
                    j = j.next
            else:
                j = j.next
        i = i.next
        j = i


ll = LinkedList([1,3,5,3,2, 7,7,2,5, 8, 9])

print(ll)

remove_dups_follow_up(ll)

print(ll)
