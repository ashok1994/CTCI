"""
    There are three types of edits that can be performed on strings: insert a character, remove a character,
    or replace a character . Given a strings , write a function to check if they are one edit(or zero edits away)

"""

import unittest


def checkOneEdit(source, target):
    source = list(source)
    target = list(target)

    if abs(len(source) - len(target)) > 1:
        return False

    not_matched = 0
    for char in target:
        if char in source:
            source.remove(char)
        else:
            not_matched += 1

        if not_matched > 1:
            return False

        if len(source) == 0:
            break

    if len(source) <= 1:
        return True
    else:
        return False


class TestOneAway(unittest.TestCase):
    data = data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test(self):
        for [str1, str2, expected] in self.data:
            res = checkOneEdit(str1, str2)

            self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
