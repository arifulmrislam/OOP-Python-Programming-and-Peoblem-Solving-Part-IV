
"""
Write a python that takes a floating number from users using input() 
and outputs both Floor and Ceil of that number. 
"""
import math
num = float((input("Enter a float number: ")))

print("Floor is",math.floor(num))
print("Ceil is",math.ceil(num))

# In this program, three different variables a are defined in separate namespaces and accessed accordingly.

def outer_function():
  global a
  a = 30
  
  def inner_function():
    global a
    a = 20
    print('a=',a)
  inner_function():
    print('a=',a)

a = 10
outer_function()
print('a=',a)
