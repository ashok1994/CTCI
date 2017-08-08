"""
 Given two strings, write a method to decide if one is a permutation of the other.
"""
import unittest


def check_permutation(string1, string2):
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
    data = [
        ("ashok", "kosha", True),
        ("asd", "dsa", True),
        ("aksl", "akkl", False)
    ]
    def testUnique(self):
        for [inp1, inp2, expected] in self.data:
            res = check_permutation(inp1, inp2)
            self.assertEqual(res,expected)



if __name__ == "__main__":
    unittest.main()
