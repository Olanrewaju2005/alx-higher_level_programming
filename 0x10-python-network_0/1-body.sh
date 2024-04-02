#!/usr/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
url=$1
response=$(curl -s -o response.txt -w "%{http_code}" "$url")
if [ "$response" -eq 200 ]; then cat response.txt
fi
rm -f response.txt
