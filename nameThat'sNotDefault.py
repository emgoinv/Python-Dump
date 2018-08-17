import math
import itertools

#determines if a number is prime (1 is prime)
def isPrime(n):
    if n==1 or n==2: return True
    elif not int(n)==n or n%2==0: return False
    else:
        for x in range(3, math.ceil(math.sqrt(n))+1, 2):
            if n%x==0: return False
    return True

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

#makes a primeList
def primeList(n):
    primeList = [2]
    for x in range(3, n, 2):
        if isPrime(x): primeList.append(x)
    return primeList

#concatanates numbers to see if they are prime
def concatanation(primes):
    check = itertools.permutations(primes)
    checkInt = []
    for x in range(0, len(check)):
        checkInt.append(int(check[x]))
    if all(map(isPrime, checkInt)): return True
    else: return False
