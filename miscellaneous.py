import math

#testing recursion in python
def fibonacci(n):
    if n==0: return 0
    elif n==1: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)

#me learning how to document a function
def gen(n):
    """this is where you define stuff"""
    print(str(n)+'!')

