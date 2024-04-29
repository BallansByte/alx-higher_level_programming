#!/usr/bin/python3
"""
script takes a URL as a command line argument,sends a HTTP request to URL,
and prints the response. If the response has a status code of 400+,
it prints an error message with the status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error code: {e}")
