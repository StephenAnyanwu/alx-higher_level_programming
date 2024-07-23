#!/usr/bin/python3
"""
A python script that uses requests library to fetch
https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status')
    t = r.text
    print("Body response:")
    print("\t- type: {}".format(type(t)))
    print("\t- content: {}".format(t))
