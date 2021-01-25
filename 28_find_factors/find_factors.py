def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    upper_limit = num + 1

    # for ele in list(range(1,upper_limit):
    #     # print(num, ele)
    #     if upper_limit%ele == 0:
    #         # print(ele)
    #         factors.append(ele)
    # print(factors)
    # # return factors
    return [ele for ele in list(range(1, upper_limit)) if num%ele == 0]

# print(find_factors(10))