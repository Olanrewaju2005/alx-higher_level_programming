#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -s -o response.txt -w "%{http_code}" "$1") && [ "$response" -eq 200 ] && cat response.txt && rm -f response.txt
