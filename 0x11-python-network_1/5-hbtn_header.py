#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to
the URL and displays the value of the variable X-Request-Id
in the response header.
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
