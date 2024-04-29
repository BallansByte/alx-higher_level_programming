#!/usr/bin/python3
"""
This script takes a URL as a command line argument, sends a HTTP request to that URL,
and prints the body of the response. If the response has a status code of 400 or higher,
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
