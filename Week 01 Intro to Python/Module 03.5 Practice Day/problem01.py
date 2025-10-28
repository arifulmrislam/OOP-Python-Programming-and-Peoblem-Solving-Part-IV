""" You are given a string and your task is to swap cases. In other words, 
convert all lowercase letters to uppercase letters and vice versa.(don’t use any python built in function)
Example :  pHitrOn.iO presents "Python COuRSe".
Ans : PhITRoN.Io PRENSENTS “pYTHON coUrsE” """


CHARACTERS = "pHitrOn.iO presents “Python COuRSe“"
new_string=""

for i in range(len(CHARACTERS)):
    if(CHARACTERS[i].isupper()):
        new_string += CHARACTERS[i].lower()
    elif(CHARACTERS[i].islower()):
        new_string += CHARACTERS[i].upper()
    else:
        new_string += CHARACTERS[i]
print(new_string)
