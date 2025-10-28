""" Program to display student's marks from record"""
student_name = 'Arif'

marks = {'James': 90, 'Jules' : 95, 'Arif': 100}

for student in marks:
  if student == student_name:
    print(marks[student])
    break
else:
  print('No entry with that name found.')
