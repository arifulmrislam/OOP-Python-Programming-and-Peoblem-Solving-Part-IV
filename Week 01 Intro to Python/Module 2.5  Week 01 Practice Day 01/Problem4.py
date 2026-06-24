""" Write  a Python program to check if user entered number is ZERO,
POSITIVE or NEGATIVE until user does not want to quit """


while True:
    user_input = input("Enter a number (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    try:
        num = int(user_input)
        if(num >= 0):
            if(num == 0):
                print(num,'is Zero')
            elif(num > 0):
                print(num,'is Positive')
        elif(num < 0):
            print(num, 'is Negative')
        else:
            print('Zero')
    except ValueError:
        print("Error")

