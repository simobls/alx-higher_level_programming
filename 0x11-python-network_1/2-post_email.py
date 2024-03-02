#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

if len(sys.argv) != 3:
    print("Usage: ./2-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    # Read the content of the response and decode it in utf-8
    content = response.read().decode('utf-8')
    print(content)
