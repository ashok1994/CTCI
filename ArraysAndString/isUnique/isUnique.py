import unittest


def isUnique(string):
    bit_vector = [False for i in range(256)]

    for char in string:
        if bit_vector[ord(char)]:
            return False
        else:
            bit_vector[ord(char)] = True

    return True


class TestIsUnique(unittest.TestCase):
    def testUnique(self):
        res = isUnique("ashok")
        self.assertTrue(res)

        res = isUnique("aashok")
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
