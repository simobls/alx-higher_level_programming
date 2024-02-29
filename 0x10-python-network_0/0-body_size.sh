#!/bin/bash

# Check if URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from command line argument
url=$1

# Use curl to send a request and get the size of the response body
size=$(curl -sI "$url" | grep -i content-length | awk '{print $2}' | tr -d '\r')

# Check if size is obtained successfully
if [ -z "$size" ]; then
    echo "Error: Unable to get response size for $url"
    exit 1
fi

echo "$size"
