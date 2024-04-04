#!/usr/bin/python3

""" sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""

if __name__ == "__main__":
    from requests import post
    from sys import argv

    url = argv[1]
    email = argv[2]
    r = post(url, {'email': email})
    print(r.text)
