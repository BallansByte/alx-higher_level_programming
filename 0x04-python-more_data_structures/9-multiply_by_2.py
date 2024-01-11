def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Parameters:
        a_dictionary (dict): The input dictionary with integer values.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
