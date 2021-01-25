def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    # given tuple
    # return t or f
    list_a = list(a)
    list_b = list(b)

    a_len = len(list_a)
    b_len = len(list_b)

    if a_len <=2 or b_len <= 2:
        return False

    for ele in list_a[2]:
        for item in list_b[2]:
            if item == ele:
                return True
      
    return False

elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

# print(friend_date(elmo, sauron))

# print(friend_date(sauron, gandalf))