""" 
Write a program to check if the given number is a palindrome number.
Input : 121
Output : True
"""

num1 = input(str("Enter a number: "))
num2 = str(num1[::-1])

if num1 == num2:
    print(True)
else:
    print(False)
