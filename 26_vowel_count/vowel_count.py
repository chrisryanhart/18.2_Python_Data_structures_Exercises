def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    lowercased = phrase.lower()
    split_phrase = lowercased.split(" ")
    # print('split phrase: ',split_phrase)
    joined = "".join(split_phrase)
    # print(joined)
    phrase_set = set(joined)

    # print(phrase_set)
    vowels = 'aeiou'

    vowel_dict = {}

    # has to count repeats
    # take to lowercase

    for char in vowels:
        count = joined.count(char)
        # print(count)
        if joined.count(char) != 0:
            vowel_dict[char] = joined.count(char)
    

    # for ele in phrase_set:
    #     vowel_dict[ele] = joined.count(ele)
    
    return vowel_dict


# print(vowel_count('HOW ARE YOU? i am great!'))