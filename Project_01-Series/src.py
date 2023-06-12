import math
from math import *
def a(n):
    return (9/(2*sqrt(3)))*((factorial(n)**2)/factorial(2*n+1))

def b(n):
    return 4*(((-1)**n)/(2*n+1))

# exercicio 2

def a(n):
    return (9/(2*sqrt(3)))*(factorial(n)**2)/factorial(2*n+1)

def prog1(eps):
    n = 0
    s = 0 
    while a(n)*(4/3) > eps :
        s += a(n)
        n += 1
    return (s,n)

# exercicio 3


def b(n):
    return 4*(((-1)**n)/(2*n+1))


def prog2(eps):
    n = 0
    s = 0 
    while abs(b(n)) > eps :
        s += b(n)
        n += 1
    return (s,n)

#for i in range (8,16):
#    print (10**-i,prog2(10**-i))

# exercicio 4

"""para a série em 2"""
def newprog1(eps):
    n = 0
    s = 0 
    while a(n)*(4/3) > eps :
        s += a(n)
        n += 1
    return (abs(pi-s),s,n)

""" para a série em 3 """

def newprog2(eps):
    n = 0
    s = 0 
    while abs(b(n)) > eps :
        s += b(n)
        n += 1
    return (abs(pi-s),s,n)
