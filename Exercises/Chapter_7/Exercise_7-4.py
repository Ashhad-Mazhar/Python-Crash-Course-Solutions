while topping != 'quit':
    topping = input('Enter a topping or type "quit" to quit: ')
    if topping == 'quit':
        break
    else:
        print(f'We will add {topping} to your pizza.')