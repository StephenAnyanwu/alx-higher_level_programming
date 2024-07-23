#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the
URL and displays:
- The body of the response if there are no errors
- The error code when there is an HTTP error.
"""


if __name__ == "__main__":
    import requests
    import sys

    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
