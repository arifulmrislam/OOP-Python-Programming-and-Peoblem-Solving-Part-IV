# def total_cost(price, quantity):
#     cost = price * quantity
#     return cost

# pay = total_cost(10,3)
# print(f'total cost:{pay}')

balance = 580

def total_cost(price, quantity):
    global balance
    cost = price * quantity
    balance = balance - cost
    return cost

print(f'balance: outside before: {balance}')

pay = total_cost(10,3)
print(f'please pay: {pay}')

print(f'balance: outside after: {balance}')
