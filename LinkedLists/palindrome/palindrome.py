"""
    Implement a function to check if a linked list is a palindrome
"""
from LinkedLists.LinkedList import LinkedList



def check_palindrome(ll):
    stack = []
    i = 0
    list_len = len(ll)
    odd_len = list_len % 2 != 0
    for item in ll:
        if odd_len and i == list_len//2:
            i+=1
            continue
        i+=1

        if len(stack) > 0:
            val = stack.pop()
            if(val == item):
                continue
            else:
                stack.append(val)
                stack.append(item)
        else:
            stack.append(item)

    return len(stack) == 0


link_l = LinkedList([1,4,4,4,4,1])

print(check_palindrome(link_l))




