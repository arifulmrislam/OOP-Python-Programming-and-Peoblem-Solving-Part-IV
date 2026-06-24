
"""
Suppose you have a floating number N.1 then.
Floor is the greatest integer less than or equal to N. And Ceil is the smallest number greater than or equal to N.1
Example: for 3.4 Floor is 3 and Ceil if 4
"""
import math
num = float((input("Enter a float number: ")))

floor_val = math.floor(num)
ceil_val = math.ceil(num)

print(f"Floor is {floor_val}")
print(f"Ceil is {ceil_val}")














# In this program, three different variables a are defined in separate namespaces and accessed accordingly.

# def outer_function():
#     global a
#     a = 30
# 
#     def inner_function(): 
#         global a
#     a = 20
#     print('a=',a)
#     inner_function():
#     print('a=',a)
# 
# a = 10
# outer_function()
# print('a=',a)
