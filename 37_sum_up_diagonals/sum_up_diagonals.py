def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # one var will count up
    # another var will count down
    sum = 0
    length = len(matrix[0])
    # print(length)

    idx_1 = length -1
    idx_2 = 0

    for ele in matrix:
        # print(idx_1, idx_2)
        sum += ele[idx_1] + ele[idx_2]
        idx_1 -= 1
        idx_2 += 1
    return sum

# m2 = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],
# ]

# print(sum_up_diagonals(m2))