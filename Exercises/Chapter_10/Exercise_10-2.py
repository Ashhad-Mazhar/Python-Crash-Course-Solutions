lines = []

with open('learning_python.txt') as my_file:
    for line in my_file:
        print(line.replace('Python', 'C'))