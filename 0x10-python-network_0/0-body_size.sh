#!/usr/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

response=$(mktemp)
curl -s -o "$response" "$1"

size=$(stat -c '%s' "$response")

echo "$size"

rm "$response"
