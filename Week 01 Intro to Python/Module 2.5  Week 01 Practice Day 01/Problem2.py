"""Write a function that takes 3 integer inputs from user and outputs absolute values of these integers without
using any library function"""
def findAbsolute(n):
    if n < 0:
        n *= -1
    print (n)

n = int(input())
findAbsolute(n)
n = int(input())
findAbsolute(n)
n = int(input())
findAbsolute(n)