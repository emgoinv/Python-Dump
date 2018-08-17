import math

#determines if a number is prime (1 is prime)
def isPrime(n):
    if n==1 or n==2: return True
    elif not int(n)==n or n%2==0: return False
    else:
        for x in range(3, int(math.sqrt(n)+1), 2):
            if n%x==0: return False
    return True

#determines if a number is a Gaussian Prime
def isGPrime(n):
    if n.real == 0:
        if isPrime(abs(n.imag)) and abs(n.imag)%4==3: return True
    elif n.imag == 0:
        if isPrime(abs(n.real)) and abs(n.real)%4==3: return True
    else:
        if isPrime(n.real**2+n.imag**2): return True
    return False

#returns the greatest factor
def greatestFactor(n):
    for x in range(2, int(n/2)):
        if n/x==int(n/x): return int(n/x)

#returns the greatest prime factor (PE #3)
def primeFactor(n):
    x = greatestFactor(n)
    while greatestFactor(x) is not None: x = greatestFactor(x)
    print (x)

#sum of all primes below 2000000
def primeSum():
    primeList = [2]
    for p in range(3, 2000000, 2):
        if isPrime(p): primeList.append(p)
    print(sum(primeList))
