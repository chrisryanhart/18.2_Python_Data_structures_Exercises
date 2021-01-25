def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    # loop through list and capture highest 
    # save highest and second highest
    # return tuple
    import copy

    sec_highest = 0
    highest = 0

    for age in ages:
        if age > highest:
            sec_highest = copy.copy(highest)
            # print('2nd highest = ',sec_highest)

            highest = age
            # print('highest = ', highest)
        elif age > sec_highest and age != highest:
            sec_highest = age

    return (sec_highest, highest)


# print(two_oldest_ages([1, 2, 10, 8]))

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.