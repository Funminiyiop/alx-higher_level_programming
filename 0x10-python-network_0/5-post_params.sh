#!/bin/bash
# This takes in URL, sends POST request to the URL, and displays the body of the response. A variable 'email' = 'test@gmail.com'. A variable 'subject' = 'I will always be here for PLD'.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
