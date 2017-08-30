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

num1 = LinkedList([9,7,8])
num2 = LinkedList([6,8,5])

print(sum_list(num1,num2))
