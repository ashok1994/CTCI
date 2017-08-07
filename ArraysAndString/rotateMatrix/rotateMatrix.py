"""
    Rotate Matrix :
    Given an image represented by N x N , where each pixel in the image is 4 bytes, write a method to rotate
    the image by 90 degrees.
    Can you do this in place?

"""
import unittest


def getNewValue(matrix, x, y):
    size = len(matrix)
    x_new = y
    y_new = (size - 1) - x
    return (x_new, y_new)


def swap(matrix, init_x, init_y, init_val):
    (new_x, new_y) = getNewValue(matrix, init_x, init_y)
    value = matrix[new_x][new_y]
    matrix[new_x][new_y] = init_val
    return ((new_x, new_y), value)


def swap_four(matrix, x, y):
    new_x = x
    new_y = y
    new_value = matrix[x][y]
    for i in range(4):
        ((new_x, new_y), new_value) = swap(matrix, new_x, new_y, new_value)


def rotate(matrix):
    for j in range(int(len(matrix) / 2)):
        for i in range(j, len(matrix) - 1 - j):
            swap_four(matrix, j, i)

    return matrix


class TestRotateMatrix(unittest.TestCase):
    data = [
        (
            [
                [1, 2, 3, 4, 9],
                [5, 6, 7, 8, 2],
                [9, 10, 11, 12, 122],
                [13, 14, 15, 16, 46],
                [9, 23, 4, 2, 1]
            ],
            [
                [9, 13, 9, 5, 1],
                [23, 14, 10, 6, 2],
                [4, 15, 11, 7, 3],
                [2, 16, 12, 8, 4],
                [1, 46, 122, 2, 9]
            ]
        ),
        (
            [
                [1, 2, 3],
                [2, 3, 4],
                [3, 4, 5]
            ],
            [
                [3, 2, 1],
                [4, 3, 2],
                [5, 4, 3]
            ]
        ),
        (
            [
                [1, 2],
                [2, 3]
            ],
            [
                [2, 1],
                [3, 2]
            ]
        ),
        (
            [[1]],
            [[1]]
        )
    ]

    def test(self):

        for (matrix, expected) in self.data:
            copy_matrix = matrix[:]
            rotate(copy_matrix)
            self.assertEqual(copy_matrix, expected)


if __name__ == '__main__':
    unittest.main()
