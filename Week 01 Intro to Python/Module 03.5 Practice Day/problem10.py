""" Write a program to print the following star pattern using the for loop
Input : 5
Output :
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
rows = 5

for i in range(rows):
    for j in range(i+1):
        print("*",end=' ')
    print('')

for i in range(rows):
    for j in range(i,rows-1):
        print("*",end=' ')
    print('')