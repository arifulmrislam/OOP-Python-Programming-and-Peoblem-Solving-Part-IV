"""
2. Write a python to read three floating numbers from the keyboard in a single line with ‘-’ (dash) in between and output their sum.

Example input:
>> enter numbers: 2.3-4.5-1.7

Example Output:
>> sum is: 8.5
"""


a,b,c = list(map(float,input().split('-')))

print(a+b+c)

a,b,c = [float(x)for x in input().split("-")]

print(a+b+c)



