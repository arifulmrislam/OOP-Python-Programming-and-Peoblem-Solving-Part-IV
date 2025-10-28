""" In the famous Rock Paper Scissor game - ROck wins against scissors, paper wins against rock, and  Scissors
wins against paper """
x1 = input("Player 1: ")
x2 = input("Player 2: ")

if(x1 == 'rock' and x2 == 'paper'):
    print("Player 2 is the winner")
elif(x1 == 'rock' and x2 == 'scissors'):
    print("Player 1 is the winner")
elif(x1 == 'scissors' and x2 == 'paper'):
    print("Player 1 is the winner")
else:
    print('Looks like an invalid input')
