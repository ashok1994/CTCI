"""
    Implement a algorithm to determine, if a string has all unique characters
"""
import unittest


def is_unique(string):
    # Create bit vector for all possible characters
    bit_vector = [False for i in range(256)]

    # Set the bit to true , if already True -> Found a duplicate
    # ord(char) -> Gives ascii value of a character
    for char in string:
        if bit_vector[ord(char)]:
            return False
        else:
            bit_vector[ord(char)] = True

    return True


class TestIsUnique(unittest.TestCase):
    def testUnique(self):
        res = is_unique("ashok")
        self.assertTrue(res)

        res = is_unique("aashok")
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
