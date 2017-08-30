"""
    Sum Lists : You have two numbers represented by a linked list , where each node contains
    a single digit .The digits are stored in reverse order, such that the 1's digit is at the
    head of the list. Write a function that adds the two numbers and returns the sum as linked list.
"""
from LinkedLists.LinkedList import LinkedList


def sum_list(LL1:LinkedList, LL2:LinkedList):
    carry = 0
    head1 = LL1.head
    head2 = LL2.head
    sum_ll = LinkedList()
    while head1 is not None and head2 is not None:
        val_a = head1.data
        val_b = head2.data
        total = val_a+val_b
        total+=carry
        if total >= 10:
            sum_ll.add(total%10)
            carry = 1
        else:
            sum_ll.add(total)
            carry = 0
        head1 = head1.next
        head2 = head2.next

    if head1 is None:
        while head2 is not None:
            val_a = head2.data
            total = carry + val_a
            if total >= 10:
                sum_ll.add(total%10)
                carry = 1
            else:
                sum_ll.add(total)
                carry = 0
            head2 = head2.next

    elif head2 is None:
        while head1 is not None:
            val_a = head1.data
            total = carry + val_a
            if total >= 10:
                sum_ll.add(total%10)
                carry = 1
            else:
                sum_ll.add(total)
                carry = 0
            head1 = head1.next
    if carry > 0:
        sum_ll.add(carry)
    return sum_ll

num1 = LinkedList([9,7,8])
num2 = LinkedList([6,8,5])

print(sum_list(num1,num2))
