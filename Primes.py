import math

#determines if a number is prime (1 is prime)
def isPrime(n):
    isPrime = True
    if n==1 or n==2: isPrime = True
    elif not int(n)==n or n%2==0: isPrime = False
    else:
        for x in range(3, int((n+1)/2), 2):
            if n%x==0: isPrime = False
    return isPrime

#determines if a number is a Gaussian Prime
def isGPrime(n):
    prime = False
    if n.real == 0:
        if isPrime(abs(n.imag)) and abs(n.imag)%4==3:
            prime = True
    elif n.imag == 0:
        if isPrime(abs(n.real)) and abs(n.real)%4==3:
            prime = True
    else:
        if isPrime(n.real**2+n.imag**2):
            prime = True
    return prime
