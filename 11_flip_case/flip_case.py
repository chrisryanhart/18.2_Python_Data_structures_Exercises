def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # is char the to_swap var?
    # isLower? 
    # lower()/upper()
    lowered_swap = to_swap.lower()
    converted_list = []

    for char in phrase:
        lower_char = char.lower()
        if lower_char == lowered_swap:
            if char.islower():
                uppered = char.upper()
                converted_list.append(uppered)
            else:
                lowered = char.lower()
                converted_list.append(lowered)
        else:
            converted_list.append(char)
    converted_phrase = "".join(converted_list)
    return converted_phrase

    
print(flip_case('Aaaahhh', 'A'))