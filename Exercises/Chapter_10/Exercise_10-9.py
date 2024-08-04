try:
    with open('cats.txt') as cats_file:
        print('Cats:')
        for cat in cats_file:
            print(f'- {cat}')
except FileNotFoundError:
    pass

try:
    with open('dogs.txt') as dogs_file:
        print('Dogs:')
        for dog in dogs_file:
            print(f'- {dog}')
except FileNotFoundError:
    pass