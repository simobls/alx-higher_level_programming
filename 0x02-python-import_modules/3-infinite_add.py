#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    r = 0
    for i in sys.argv:
        if i != sys.argv[0]:
            r = r + int(i)
    print (r)
