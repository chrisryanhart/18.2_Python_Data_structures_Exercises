def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lowercased = phrase.lower()
    # split_str = lowercased.split(" ")



    # print(lowercased)

    return lowercased.title()

# print(titleize('oNLy cAPITALIZe fIRSt'))