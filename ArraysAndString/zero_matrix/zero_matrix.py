"""
    Write an algorithm such that if an element in M X N matrix is 0 .
    Its entire row and column
"""
import unittest
def zero_matrix(arr):

    rows = []
    cols = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                rows.append(i)
                cols.append(j)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i in rows or j in cols:
                arr[i][j] = 0

    return arr




class TestCase(unittest.TestCase):
    data = [
        (
            [
                [ 1, 0, 1],
                [ 2, 1, 0],
                [ 3, 4, 5]
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [3, 0, 0]
            ]
        )
    ]
    def test(self):
        for [matrix, expected_matrix] in self.data:
            res = zero_matrix(matrix[:])
            self.assertEqual(res, expected_matrix)


if __name__ == "__main__":
    unittest.main()
