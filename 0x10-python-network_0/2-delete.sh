#!/bin/bash
# This sends a DELETE request to a URL passed as the first argument and displays body of the response.
curl -s "$1" -X DELETE
