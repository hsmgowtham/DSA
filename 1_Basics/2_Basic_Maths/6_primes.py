'''
a number is prime number - if it can be divided by 1 and itself
'''
from math import ceil, floor, sqrt

def isPrime(n):
    for i in range(2,floor(sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
print(isPrime(n))