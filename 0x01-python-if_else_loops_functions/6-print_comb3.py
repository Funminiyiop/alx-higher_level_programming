#!/usr/bin/python3
"""
A program that prints all possible different combinations of two digits.
"""
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i < 8:
            print("{:d}{:d}".format(i, j), end=", ")
        else:
            print("{:d}{:d}".format(i, j))
