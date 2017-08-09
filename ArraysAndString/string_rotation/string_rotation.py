"""
    Assume you have a method "isSubstring()" which checks if one word is substring of another .
    Given a strings, s1 and s2 , write code to check if s2 is rotation of s1 using only one
    call to "isSubstring()"
"""
import unittest


def is_substring(string, sub):
    if sub in string:
        return True
    return False


def string_rotation(str1:str,str2:str):
    new_char = []
    index = 0
    for char in str2:
        if char == str1[index]:
            new_char.append(char)
            index+=1
            continue
        else:
            if index > 0:
                new_char = []
                index = 0
                if char == str1[index]:
                    new_char.append(char)
                    index+=1


    if len(new_char) == 0:
        return False

    if is_substring(str2,str1[index:]):
        return True

    return False


class TestStringRotation(unittest.TestCase):
    data_substring = [
        ("ashok", "ok", True),
        ("yellow", "ll", True),
        ("Hello", "alot", False)
    ]

    data_string_rotation = [
        ("waterfall","aterfallw", True),
        ("ankita", "aankit", True),
        ("assam", "ssama", True),
        ("aashok", "ashoka", True),
        ("asgok", "gokas", True),
        ("watermilkwater", "waterwatermilk", True)
    ]

    def test_is_substring(self):
        for [string, patch, expected] in self.data_substring:
            actual = is_substring(string,patch)
            self.assertEqual(actual, expected)

    def test_string_rotation(self):
        for [string1, string2, expected] in self.data_string_rotation:
            actual = string_rotation(string1, string2)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
    pass

