#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appending string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    char_count = 0
    with open(filename, 'a', encoding='utf-8') as f:
        char_count = f.write(text)
    return char_count
