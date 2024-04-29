#!/usr/bin/python3
"""
This Python script takes a URL from the command line, sends a request to that URL,
and prints the value of the 'X-Request-Id' header found in the HTTP response.
"""
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        request_id = response.getheader('X-Request-Id')
        print(request_id)
