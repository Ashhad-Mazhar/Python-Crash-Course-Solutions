import random

new_list = [
    'a', 'b', 'c', 'd', 'e', 'f','g',
    'h', 'i', 'j', 1, 2, 3, 4, 5
]

my_ticket = ['a', '2', 'e', '4']

counter = 0

while True:
    counter += 1
    sequence = []
    for i in range(0, 4):
        sequence.append(str(random.choice(new_list)))
    
    if sequence == my_ticket:
        break
    
    print(counter)

print(f'It took me {counter} times to win.')