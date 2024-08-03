def make_sandwich(*list_of_toppings):
    print('Here are your toppings:')
    for topping in list_of_toppings:
        print(f'- {topping}')

make_sandwich('mayo')
make_sandwich('mayo', 'ketchup', 'onions')
make_sandwich('garlic mayo', 'mustard sauce')