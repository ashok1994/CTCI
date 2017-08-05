import unittest


def palindromePermutation(string):
    string = string.lower()
    bit_vector = [0 for i in range(256)]

    for char in string:
        if char != " ":
            bit_vector[ord(char)] += 1

    odd_count = 0

    for val in bit_vector:
        if val % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False

    return True


# print(palindromePermutation("nothing"))
class TestPalPermute(unittest.TestCase):
    data = [
        ("Taco cat", True),
        ("madam", True),
        ("askas tobot", False),
        ("nothing", False)
    ]

    def test(self):
        for pair in self.data:
            res = palindromePermutation(pair[0])
            try:
                self.assertEqual(res, pair[1])
            except AssertionError:
                print(pair)


if __name__ == '__main__':
    unittest.main()
