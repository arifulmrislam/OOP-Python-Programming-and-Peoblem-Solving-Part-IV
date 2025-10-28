""" Count all uppercase, lowercase, digits, and special symbols from a given
"P@#yn26at^&i5ve"
Total counts of chars, digits, and symbols 

Uppercase = 1
Lowercase = 7 
Digits = 3 
Symbol = 4
"""
s = "P@#yn26at^&i5ve"
Uppercase = 0
Lowercase = 0
Digits = 0
Symbol = 0

for i in s:
    if i.isupper():
        Uppercase += 1
    elif i.islower():
        Lowercase += 1
    elif i.isdigit():
        Digits += 1
    else:
        Symbol += 1
print(Uppercase)
print(Lowercase)
print(Digits)
print(Symbol)