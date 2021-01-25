def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    total =0

    even_nums = [ele for ele in nums if ele%2 == 0]

    if len(even_nums) == 0:
        return 1
    for num in even_nums:
        if total == 0:
            total = num
        else:
            total = total * num
    return total

# print(multiply_even_numbers([1, 3, 5])) 