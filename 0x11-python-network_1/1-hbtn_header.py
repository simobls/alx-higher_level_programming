#!/usr/bin/python3

import urllib.request
import sys

if len(sys.argv) == 2:
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
