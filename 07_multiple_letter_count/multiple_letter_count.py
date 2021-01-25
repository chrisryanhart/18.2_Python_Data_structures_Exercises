def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    chars = set(phrase)
    pairs = {}
    for char in chars:
        count = phrase.count(char)
        pairs[char] = count
    return pairs
print(multiple_letter_count('valencia'))