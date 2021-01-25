def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    # if bool is true, place in ok list
    # if bool is false, place in NG list 

    # have to determine if fn is true or false
    # must pass fn test criteria
    t_list = []
    f_list = []

    # print(bool(fn))

    for ele in lst:
        if fn(ele):
            t_list.append(ele)
        else:
            f_list.append(ele)
    return [t_list, f_list]

def is_even(num):

    return num % 2 == 0
    
def is_string(el):
    return isinstance(el, str)

# print(partition([1, 2, 3, 4], is_even))