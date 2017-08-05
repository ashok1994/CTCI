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

    for char in target:
        if char in source:
            source.remove(char)

        if len(source) == 0:
            break

    if len(source) <= 1:
        return True
    else:
        return False


class TestOneAway(unittest.TestCase):
    data = [
        (('pale', 'ple'), True),
        (('pales', 'pale'), True),
        (('pale', 'bale'), True),
        (('pale', 'bake'), False)
    ]

    def test(self):
        for case in self.data:
            res = checkOneEdit(case[0][0], case[0][1])
            self.assertEqual(res, case[1])


if __name__ == '__main__':
    unittest.main()
