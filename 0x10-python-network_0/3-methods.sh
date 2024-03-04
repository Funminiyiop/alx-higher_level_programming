#!/bin/bash
# Takes in a URL and displays all the HTTP methods the server will accept.
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
