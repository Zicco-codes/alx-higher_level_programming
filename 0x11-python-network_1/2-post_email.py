#!/usr/bin/python3

"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    argv = sys.argv
    url = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')

    with urlib.request.urlopen(url, data) as r:
        print(r.read().decode('utf-8'))
