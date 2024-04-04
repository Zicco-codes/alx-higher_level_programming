#!/usr/bin/python3

""" displays the value of the X-Request-Id variable """

if __name__ == "__main__":
    import sys
    import urllib.request

    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    with urllib.request.urlopen(url) as r:
        print(r.headers["X-Request-Id"])
