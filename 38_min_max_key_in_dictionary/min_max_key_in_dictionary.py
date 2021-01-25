def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    # return tuple of min & max keys
    # sort list 
    # take first index and last
    # 

    keys = list(d.keys())
    keys.sort()
    # print(sorted_keys)
    # print(keys)


    k_length = len(keys)
    max_idx = k_length - 1

    min = keys[0]
    max = keys[max_idx]

    return (min, max)

# my_dict = {2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}

# print(min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))
     

  