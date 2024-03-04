#!/bin/bash
# Takes a URL, sends request to the URL, displays the size of body of the response.
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
