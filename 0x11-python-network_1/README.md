# Network #1

# Learning Objectives

- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` #requestsiswaysimplerthanurllib
- How to make HTTP `GET` request
- How to make HTTP `POST`/`PUT`/etc. request
- How to fetch JSON resources
- How to manipulate data from an external service

# Tasks

## What's my status? #0

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- You must use the package `urllib`
- You are not allowed to import any packages other than `urllib`
- The body of the response must be displayed like the following example (tabulation before -)
- You must use a `with` statement

**Solution:** [0-hbtn_status.py](./0x11-python-network_1/0-hbtn_status.py)

## Response header value #0

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.

- You must use the packages `urllib` and `sys`
- You are not allow to import packages other than `urllib` and `sys`
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a `with` statement

**Solution:** [1-hbtn_header.py](./0x11-python-network_1/1-hbtn_header.py)

## POST an email #0

Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)

- The email must be sent in the `email` variable
- You must use the packages `urllib` and `sys`
- You are not allowed to import packages other than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

**Solution:** [2-post_email.py](./0x11-python-network_1/2-post_email.py)

## Error code #0

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).

- You have to manage `urllib.error.HTTPError` exceptions and print: `Error code`: followed by the HTTP status code
- You must use the packages `urllib` and `sys`
- You are not allowed to import other packages than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the `with` statement

**Solution:** [3-error_code.py](./0x11-python-network_1/3-error_code.py)

## What's my status? #1

Write a Python script that fetches `https://alx-intranet.hbtn.io/status`

- You must use the package `requests`
- You are not allow to import packages other than `requests`
- The body of the response must be display like the following example (tabulation before `-`)

**Solution:** [4-hbtn_status.py](./0x11-python-network_1/4-hbtn_status.py)

## Response header value #1

Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header

- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)

**Solution:** [5-hbtn_header.py](./0x11-python-network_1/5-hbtn_header.py)

## POST an email #1

Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.

- The email must be sent in the variable `email`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to error check arguments passed to the script (number or type)

**Solution:** [6-post_email.py](./0x11-python-network_1/6-post_email.py)

## Error code #1

Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)

**Solution:** [7-error_code.py](./0x11-python-network_1/7-error_code.py)

## Search API

Write a Python script that takes in a letter and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.

- The letter must be sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
- Otherwise:
  - Display `Not a valid JSON` if the JSON is invalid
  - Display `No result` if the JSON is empty
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`

**Solution:** [8-json_api.py](./0x11-python-network_1/8-json_api.py)

## My Github!

Write a Python script that takes your Github credentials (username and password) and uses the [Github API](https://developer.github.com/v3/users/#get-the-authenticated-user) to display your `id`

- You must use [Basic Authentication](https://developer.github.com/v3/auth/#basic-authentication) with a [personal access token as password](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to access to your information (only `read:user` permission is needed)
- The first argument will be your username
- The second argument will be your password (in your case, a [personal access token as password](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token))
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)

**Solution:** [10-my_github.py](./0x11-python-network_1/10-my_github.py)

## Time for an interview!

```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the Github API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```

Write a Python script that takes 2 arguments in order to solve this challenge.

- The first argument will be the `repository name`
- The second argument will be the `owner name`
- You must use the packages `requests` and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to check arguments passed to the script (number or type)

**Solution:** [100-github_commits.py](./0x11-python-network_1/100-github_commits.py)
