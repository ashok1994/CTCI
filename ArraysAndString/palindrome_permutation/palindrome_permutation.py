"""
Given a string , write a function to check if it is a permutation of the other.

"""

import unittest


def palindrome_permutation(string):
    # Convert to lower
    string = string.lower()

    # Create a bit vector
    bit_vector = [0 for i in range(256)]

    # Count frequency of characters
    for char in string:
        if char != " ":
            bit_vector[ord(char)] += 1


    odd_count = 0
    # More than one odd frequency character -> Cannot form a palindrome
    for val in bit_vector:
        if val % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False

    return True



class TestPalPermute(unittest.TestCase):
    data = [
        ("Taco cat", True),
        ("madam", True),
        ("askas tobot", False),
        ("nothing", False)
    ]

    def test(self):
        for pair in self.data:
            res = palindrome_permutation(pair[0])
            try:
                self.assertEqual(res, pair[1])
            except AssertionError:
                print(pair)


if __name__ == '__main__':
    unittest.main()
