def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    # loop through elements
    # are the subsequent elements larger?
    # make copy of list
    # iterate through one list

    # or start by getting length
    # make list with range of 
    # 
    # can also find index
    
    length = len(nums)
    counter = 1
    greater = 0

    for num in nums:
        for ele in range(length):
            if ele >= counter and num < nums[ele]:
                greater += 1
        counter += 1
    return greater

# print(find_greater_numbers([]))
        
        # for ele in copy:
