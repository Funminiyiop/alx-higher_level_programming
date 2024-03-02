t config merge.conflictstyle diff3
git config mergetool.prompt false

#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
with `requests`.

If the HTTP status code is > or = 400, print: Error 
code: followed by value of HTTP status code
"""

from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])

    if req.status_code >= 400:
<<<<<<< HEAD
        print("Error code: {}".format(req.status_code))
>>>>>>> 0724e0ab7231df912c454aad35091c949c2fcaa7
    else:
        print(req.text)
