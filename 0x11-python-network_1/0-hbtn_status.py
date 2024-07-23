#!/usr/bin/python3
"""
A python script that uses urllib package to fetch
https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response")
        print(f"\t- type: {type(content)}")
        print(f"\t- type: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
