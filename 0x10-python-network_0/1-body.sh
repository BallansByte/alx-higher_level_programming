#!/bin/bash
# Sends a GET request to a given URL and displays the body of the response if the status code is 200
curl -s -o response.txt -w "%{http_code}" $1 | grep -q "^200$" && cat response.txt && rm response.txt || rm response.txt
