#!/usr/bin/python3
"""
A Python script that takes user's GitHub credentials
(username and password) and uses the GitHub API to
display the user's id.
First argument: username
Second argument: password (personal access token)
"""


if __name__ == "__main__":
    import sys
    from requests import get, auth

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(username, password))
    print(r.json().get('id'))
