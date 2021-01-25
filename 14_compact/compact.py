def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    false_removed = [ele for ele in lst if bool(ele)]
    return false_removed

# print(compact([0, 1, 2, '', [], False, (), None, 'All done']))