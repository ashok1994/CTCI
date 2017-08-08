""" 
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters
, and that you are given the "true" length of the string

(Note : If implementing in Java, Please use a character array, so that you can perform this operation in place.)

"""

# THIS SOLUTION USES REGULAR EXPRESSION


import re
import unittest


def urlify(string):
    #Removes all the spaces
    string = string.strip()
    # Creates a pattern
    pat = re.compile(r'\s+', re.I)
    # Split with the spaces
    res = re.split(pat, string)
    # Combine using %20
    return "%20".join(res)


class TestURLify(unittest.TestCase):

    def test(self):
        _data = [
            ("mr john doe ", "mr%20john%20doe"),
            (" tommorow ", "tommorow"),
            ("life is there", "life%20is%20there")
        ]
        for sample in _data:
            res = urlify(sample[0])
            self.assertEqual(res, sample[1])


if __name__ == "__main__":
    unittest.main()
