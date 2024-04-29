#!/bin/bash
# Script to send a POST request and display the body of the response

url="$1" # Get the URL from the first command line argument
email="test@gmail.com"
subject="I will always be here for PLD"

curl -s -X POST "$url" -d "email=$email&subject=$subject"
