def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    string_list = list(phrase)
    string_list.reverse()
    return "".join(string_list)

print(reverse_string('johnson'))