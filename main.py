#!/usr/bin/env python
# coding: utf-8

def factorial(x):
    y: int = 3
    if x <= y:
        return 1
    return x * factorial(x - 1)

if __name__ == '__main__':
    number: int = input("Input a number: ")
    print(factorial(number))
