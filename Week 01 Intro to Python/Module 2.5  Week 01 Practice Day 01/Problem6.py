# rows = 6
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for x in range(rows):
#     # nested loop
#     for y in range(x):
#         # display number
#         print(x, end=' ')
#     # new line after each row
#     print('')


# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 
# rows = 6
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for x in range(rows):
#     # nested loop
#     for y in range(x):
#         # display number
#         print(x, end=' ')
#     # new line after each row
#     print('')
# for x in range(x-1,0,-1):
#     # nested loop
#     for y in range(0,x):
#         # display number
#         print(x, end=' ')
#     # new line after each row
#     print('')



# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
# 1 2 3 4 5 6 
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1

# rows = 6
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for x in range(1,rows+1):
#     # nested loop
#     for y in range(1,x+1):
#         # display number
#         print(y, end=' ')
#     # new line after each row
#     print('')
# for x in range(0,rows+1):
#     # nested loop
#     for y in range(1,rows-x,+1):
#         # display number
#         print(y, end=' ')
#     # new line after each row
#     print('')

# rows = 6
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for x in range(0,rows+1):
#     # nested loop
#     for y in range(1,rows-x,+1):
#         # display number
#         print(y, end=' ')
#     # new line after each row
#     print('')

    #       * 
    #      * * 
    #     * * * 
    #    * * * * 
    #   * * * * * 
    #  * * * * * *
# rows = 6
# k = 2 * rows - 2
# for i in range(0,rows):
#     for j in range(0,k):
#         print(end=' ')
#     k = k - 1
#     for j in range(0,i+1):
#         print("* ",end="")
#     print('')

# A R I F
for row in range(7):
    for col in range(5):
        if((col == 0 or col == 4) and row!=0) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
            print("*",end ="")
        else:
            print(end=" ")
    print()
print()
for row in range(7):
    for col in range(7):
        if(col == 0 or ((row == 0 or row == 3) and col > 0 and col <5) or (col ==5 and row !=0 and row < 3) or (col == row -1 and row >2)):
            print('*',end="")
        else:
            print(end=" ")
    print()
print()
for row in range(7):
    for col in range(7):
        if((col == 3) and (row !=2)):
            print("*",end="")
        else:
            print(end=" ")
    print()
print()
for row in range(7):
    for col in range(7):
        if(col == 0 or (row == 0 or row == 3)):
            print("*",end="")
        else:
            print(end="")
    print()
print()
