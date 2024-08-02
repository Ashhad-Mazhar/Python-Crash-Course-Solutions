print('We have run out of pastrami')

sandwich_orders = [
    'tuna',
    'pastrami',
    'chicken',
    'pastrami',
    'pastrami',
    'club'
]
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    if order != 'pastrami':
        print(f'I made your {order} sandwich.')
        finished_sandwiches.append(order)

print('All sandwiches have been made.')