"""
    Remove Dups :
    Write code to remove duplicate from an unsorted list. --> remove_dups()
    Follow up
    How would you solve this problem if a temporary buffer is not allowed ? --> remove_dups_b()
"""

import unittest

class Node:
    def __init__(self, number):
        self.data = number
        self.next = None

    def __str__(self):
        return "Node({})".format(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        # Returns formatted LinkedList
        if self.head is None:
            return "(empty)"
        else:
            string = ""

            # First Node
            curr = self.head
            string += str(curr.data)+" -> "

            # Iterate through all nodes
            while curr.next is not None:
                curr = curr.next
                string += str(curr.data)+" -> "

            # Null pointer of last element
            string += "(None)"

            return string

    def append_to_tail(self, number):
        # Append a new element to the end of the linked list
        new_node = Node(number)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            # Iterate through list , until we reach end
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def return_list(self):
        if self.head is None:
            return []
        else:
            arr = []
            curr = self.head
            while curr is not None:
                arr.append(curr.data)
                curr = curr.next
            return arr
def remove_dups(linked_list:LinkedList):
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


    return linked_list


def create_linked_list(array:list):
    my_linked_list = LinkedList()
    for value in array:
        my_linked_list.append_to_tail(value)
    return my_linked_list




class TestRemoveDups(unittest.TestCase):
    data = [
        ( [1,2,3,4,5,5] , [1,2,3,4,5] ),
        ( [1,2,3,2,2,5,6] , [1, 2,3,5,6])
    ]

    def test_remove_dups(self):
        for [array, expected] in self.data:
            temp_linked_list = create_linked_list(array)
            remove_dups(temp_linked_list)
            self.assertEqual(expected, temp_linked_list.return_list())


if __name__ == "__main__":
    unittest.main()


