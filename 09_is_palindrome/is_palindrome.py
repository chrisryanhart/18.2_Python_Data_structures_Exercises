def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    split_phrase = phrase.split(" ")
    joined = "".join(split_phrase)
    joined_lowered = joined.lower()
    # print(list(joined_lowered))
    
    # reverse the string
    list_to_reverse = list(joined_lowered)
    list_to_reverse.reverse()
    # print(list_to_reverse)
    reversed_phrase = "".join(list_to_reverse)

    if reversed_phrase == joined_lowered:
        # print(reversed_phrase)
        # print(joined_lowered)
        return True
    else:
        # print(reversed_phrase)
        # print(joined_lowered)
        return False

   
    
    
#     print(joined_lowered)

# print(is_palindrome('robert'))

