def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    new_dict = {}
    print(enumerate(keys))

    key_len = len(keys)
    values_len = len(values)
    # stopping_index = 0
    counter = 0

    # if key_len - values_len > 0:
    #     stop_idx = key_len - values_len - 1
        
    # for key in keys:
    #     # if key_len > values_len:


    #     # if counter <= values_len:
    #         # new_val = values[0]
    #     print(counter)
    #     # print(values[counter])
    #     new_dict[key] = values[counter]
    #     counter = counter + 1

    # #     # else:
    # #     #     new_dict[key] = None
    # return new_dict

    # print(new_dict)
    # return new_dict

    out = {}
    counter = 0

    for idx, val in enumerate(keys):
        out[val] = values[counter] if idx < len(values) else None
        counter += 1
    return out


print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))


# Correct syntax:
# new_dict[key] = counter


a = ['a','b','c']
b = [1,2,3]