""" 
Write a program to display all prime numbers within a range. You will be given two integers l and r . 
You have to print all the prime numbers present in the given range l and r.
Input : 25 50

Output :
29
31
37
41
43
47
"""

num1 = 25
num2 = 50

for num in range(num1,num2+1):
    if num > 1:
        for i in range(2,num):
            if(num % i== 0):
                break
        else:
            print(num)