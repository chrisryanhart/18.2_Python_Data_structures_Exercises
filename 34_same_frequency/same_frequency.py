def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # str1 = str(num1)
    # str2 = str(num2)

    # len1 = len(str1)
    # len2 = len(str2)

    # if len1 == len2:
    #     return True
    # else:
    #     return False

# print
    return freq_counter(str(num1)) == freq_counter(str(num2))


def freq_counter(coll):
    """Returns frequency counter mapping of coll."""

    counts = {}

    for x in coll:
        counts[x] = counts.get(x, 0) + 1

    return counts




   
