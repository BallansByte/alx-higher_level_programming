#!/usr/bin/python3
"""
This script fetches data from 'https://alx-intranet.hbtn.io/status' using the urllib package.
It uses only the urllib library to make the HTTP request and prints the body of the response
in a specific formatted way as required.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
print("Body response:")
print("\t- type:", type(content))
print("\t- content:", content)
print("\t- utf8 content:", content.decode('utf-8'))
