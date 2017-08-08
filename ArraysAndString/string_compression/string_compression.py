"""
    Implement a method to perform basic string compression using the counts of repeated
    characters. 
    For example , the string aabcccccaaa would become a2b1c5a3 . If "compressed" string would not become smaller 
    than the original string , your method should return the original string. You can assume the string has only
    uppercase and lowercase letters (a-z)
"""
import unittest

# Compresses string
def compress(string):
    new_arr = [] # Holds compressed string
    count = 0
    currentChar = ''

    for char in string:
        # First Iteration
        if currentChar == '':
            currentChar = char
            count += 1

        elif currentChar != char:
            # Prev val != New Char ->
            # Time to store the prev char and count
            new_arr.append(currentChar)
            new_arr.append(str(count))
            currentChar = char
            count = 1

        else:
            # Keep increasing
            count += 1

    # Append the last character and count
    new_arr.append(currentChar)
    new_arr.append(str(count))

    # Create string
    compressed = "".join(new_arr)

    # Cannot return compressed , if it doesn't actually compresses the string
    if len(compressed) < len(string):
        return compressed
    else:
        return string


class TestStringCompression(unittest.TestCase):

    data = [
        ("aaaabb", "a4b2"),
        ("ashok", "ashok"),
        ("aaaabbb", "a4b3"),
        ("ankit", "ankit"),
        ("aeeeee", "a1e5")
    ]

    def test_compress(self):

        for [string, expected] in self.data:
            res = compress(string)
            self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
