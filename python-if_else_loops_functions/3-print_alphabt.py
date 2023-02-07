#!/usr/bin/python3
# 3-print_alphabt.py

for xup in range(ord('a'), ord('z') + 1):
    if chr(xup) != 'q' and chr(xup) != 'e':
        print("{}".format(chr(xup)), end='')
