sandwich_orders = ['tuna sandwich', 'chicken sandwich', 'club sandwich']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'I made your {order}')
    finished_sandwiches.append(order)

print('All sandwiches have been made.')