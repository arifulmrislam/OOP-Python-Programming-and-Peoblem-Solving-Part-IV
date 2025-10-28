""" Clean the data and get a String output 'a e i o u' """
data = "aNtEriOur\n\t>>"

new_data = data.lower()
update_data = ''

for char in new_data:
    if(char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
        # print(f"{char} Found") 
        update_data += char + ' '
print(update_data)