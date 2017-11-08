"""
    Sum Lists : You have two numbers represented by a linked list , where each node contains
    a single digit .The digits are stored in reverse order, such that the 1's digit is at the
    head of the list. Write a function that adds the two numbers and returns the sum as linked list.
"""
from LinkedLists.LinkedList import LinkedList

def get_sum_and_carry(a,b,carry):
    total = sum([a,b])
    total = sum([total,carry])

    if total >= 10:
        return (total%10, 1)
    else:
        return total,0


def sum_list(LL1:LinkedList, LL2:LinkedList):
    carry = 0
    head1 = LL1.head
    head2 = LL2.head
    sum_ll = LinkedList()
    while head1 is not None and head2 is not None:
        val_a = head1.data
        val_b = head2.data
        (s, carry) = get_sum_and_carry(val_a, val_b, carry)
        sum_ll.add(s)
        head1 = head1.next
        head2 = head2.next

    if head1 is None:
        while head2 is not None:
            val_a = head2.data
            (s, carry) = get_sum_and_carry(val_a,0,carry)
            sum_ll.add(s)
            head2 = head2.next

    elif head2 is None:
        while head1 is not None:
            val_a = head1.data
            (s, carry) = get_sum_and_carry(val_a, 0, carry)
            sum_ll.add(s)
            head1 = head1.next
    if carry > 0:
        sum_ll.add(carry)
    return sum_ll

# Follow Up

class PartialSum():
    def __init__(self):
        self.sum = LinkedList()
        self.carry = 0


def sum_list_follow_up(link1, link2):
    if len(link1) < len(link2):
        padList(link1, len(link2))
    elif len(link1) > len(link2):
        padList(link2, len(link1))

    return add_util(link1.head, link2.head).sum


def add_util(head1, head2):
    if head1 == None and head2 == None:
        return PartialSum()
    partial_sum = add_util(head1.next, head2.next)
    total = partial_sum.carry + head1.data + head2.data
    if total >= 10:
        partial_sum.sum.add_to_beginning(total%10)
        partial_sum.carry = 1
    else:
        partial_sum.sum.add_to_beginning(total)
        partial_sum.carry = 0
    return partial_sum



def padList(link1:LinkedList, length):
    while len(link1) != length:
        link1.add_to_beginning(0)




num1 = LinkedList([9,7,8, 9, 1])
num2 = LinkedList([6,8,5])

print(sum_list_follow_up(num1,num2))
