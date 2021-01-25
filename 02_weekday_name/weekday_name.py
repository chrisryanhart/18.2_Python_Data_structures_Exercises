def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # lists, sets, dict, Tuples 
    day_numbers = {1,2,3,4,5,6,7} 
    day_dict = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}

    if day_of_week not in day_numbers:
        print('not a day')
        return None
    else:
        return day_dict[day_of_week]



print(weekday_name(4))