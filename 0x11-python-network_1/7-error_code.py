#!/usr/bin/python3

""" sends a request to the URL and displays the body of the response. """

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = argv[1]

    r = get(url)
    err = 'Error code: {}'
    status = r.status_code
    print(err.format(status) if (status >= 400) else r.text)
