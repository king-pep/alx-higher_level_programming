#!/usr/bin/python3

 def uppercase(str1):
    for i in str1:
        if 97 <= ord(i) <= 122:
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
    print()
