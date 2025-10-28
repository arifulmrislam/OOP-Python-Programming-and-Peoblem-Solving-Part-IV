""" Write a program to print the following number pattern using a loop.
Input : 5
Output : 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""

rows = 5

for i in range(rows+1):
    for j in range(1,i+1):
        # print (i,end=' ')
        print (j,end=' ')
    print('')