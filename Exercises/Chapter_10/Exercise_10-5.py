names = []

while True:
    input_name = input('What is your name? ')
    if input_name == 'quit':
        break
    print('IT DOESNT MATTER WHAT YOUR NAME IS!')
    names.append(input_name)

try:
    with open('guest_book.txt', 'a') as my_file:
        for name in names:
            my_file.write(f'{name}\n')
except FileNotFoundError:
    print('File does not exist')