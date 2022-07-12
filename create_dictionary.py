def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    # for x,y in key,value:
    #     dict1={x:y}
    # return dict1
    for x in key:
        for y in value:
            name={x:y}
    print(name)
create_dictionary([1,2,3],["a","b","c"])