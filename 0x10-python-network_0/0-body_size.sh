#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
response=$(curl -sI "$1") && echo "$response" | grep -i Content-Length | awk '{print $2}'
