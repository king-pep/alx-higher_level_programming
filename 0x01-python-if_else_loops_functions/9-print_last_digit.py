#!/usr/bin/python3
def print_last_digit(number1):
    if number1 < 0:
        last_digit1 = number1 % -10
    else:
        last_digit1 = number1 % 10
    print(last_digit1, end="")
    return last_digit1
