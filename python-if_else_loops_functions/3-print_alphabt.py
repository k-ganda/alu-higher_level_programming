#!/usr/bin/python3
# 3-print_alphabt.py

for alpha_letters in range(ord('a'), ord('z')+1):
    if chr(alpha_letters) == 101 or 113:
       continue
    print("{:c}".format(alpha_letters), end="")
