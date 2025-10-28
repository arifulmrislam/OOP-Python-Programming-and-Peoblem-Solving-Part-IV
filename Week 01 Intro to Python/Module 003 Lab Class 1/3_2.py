""" Encrypt the following code so that no one can get your strategy """

data = 'firebaby'
shift = 4
output = ' '
for char in data:
    output += chr((ord(char)+shift-97) % 26 + 97)
print(output)