""" Write  a Python program to check if user entered number is ZERO,
POSITIVE or NEGATIVE until user does not want to quit """

num = (input("Enter input: "))
if (num == 'Quit'):
    print('(Stop the program)')
elif(int(num) >= 0):
    if(int(num) == 0):
        print(num,'is Zero')
    elif(int(num > 0):
         print(num,'is Positive')
elif(int(num) < 0):
    print(num, 'is Negative')
else:
    print('Zero')
