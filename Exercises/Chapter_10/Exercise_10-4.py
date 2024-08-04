name = input('What is your name? ')

with open('guest.txt', 'w') as my_file:
    my_file.write(name)

print("IT DOESN'T MATTER WHAT YOUR NAME IS!")