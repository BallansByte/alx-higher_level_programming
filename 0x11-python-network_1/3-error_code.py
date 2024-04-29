#!/usr/bin/python3
"""
taking a URL as a command-line argument, sends a request to URL,
and displays the body of the response decoded in utf-8. manages HTTP errors

Using urllib to fetch the URL
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print(content.decode('utf-8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
