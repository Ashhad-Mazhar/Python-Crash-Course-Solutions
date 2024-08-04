lines = []

with open('learning_python.txt') as my_file:
    for line in my_file:
        print(line)
        lines.append(line)

print('\nFrom list:')

for line in lines:
    print(line)