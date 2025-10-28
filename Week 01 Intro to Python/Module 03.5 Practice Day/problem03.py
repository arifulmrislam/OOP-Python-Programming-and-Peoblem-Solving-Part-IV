""" 
Display Fibonacci series up to 10 terms

0  1  1  2  3  5  8  13  21  34
"""
num = 10
n1,n2 = 0,1
print("Fibonacci series:",n1,n2,end=" ")

for i in range(2,num):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3,end=' ')
print()
