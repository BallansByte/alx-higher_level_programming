#!/bin/bash

# Check if URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Assign the URL from the first argument
URL=$1

# Use curl to send a POST request with variables email and subject
curl -s -X POST $URL \
    -d "email=test@gmail.com" \
    -d "subject=I will always be here for PLD"
