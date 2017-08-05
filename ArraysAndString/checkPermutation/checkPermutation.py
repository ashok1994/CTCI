"""
 Given two strings, write a method to decide if one is a permutation of the other.
"""
import unittest


def checkPermutation(string1, string2):
    a = list(string1)
    b = list(string2)
    # Two different length of string , cannot be a permutation
    if len(a) != len(b):
        return False
    #
    for char in a:
        # if there is no occurrence of current char ( Not a permutation)
        if char not in b:
            return False
        else:
            # If there is an occurence , remove for future
            b.remove(char)
    # Check if there are chars in b or not
    if len(b) == 0:
        return True

    return False


class TestIsUnique(unittest.TestCase):
    def testUnique(self):
        res = checkPermutation("ashok", "kosha")
        self.assertTrue(res)

        res = checkPermutation("asd", "dsa")
        self.assertTrue(res)

        res = checkPermutation("aksl", "akkl")
        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
