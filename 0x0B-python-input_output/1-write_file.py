#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.
    """
    char_count = 0
    with open(filename, 'w', encoding='utf-8') as f:
        char_count = f.write(text)
    return char_count
