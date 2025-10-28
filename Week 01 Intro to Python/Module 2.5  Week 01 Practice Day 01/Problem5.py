""" Write a Python which iterates the integers from 1 to 50. For multiples of three print
"Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both
three and five print "FizzBuzz" """

def fizzbuzz(num):
    if num % 3 == 0  and num % 5 == 0:
        return 'fizzbuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    return num

for num in range(0,51):
    print(fizzbuzz(num))
    
""" Origran to find the sum of all numbers stored in a list """
#List of numbers
number = [6,5,3,8,4,2,5,4,11]

#variable to store the sum
sum = 0

#iteration over the list
for val in number:
    sum = val + sum

print("The sum is", sum)
